# coding=utf-8

# author:Tang Gaozhi

import os
import random
from flask import Flask, request, url_for, send_from_directory,jsonify

# from werkzeug import secure_filename
from werkzeug.utils import secure_filename


# import runModel
import runModel2

from constant import value2Dict, type2Dict, weights2Dict
from constant import imgUrl

import time

#保存信息用
import csv


ALLOWED_EXTENSIONS = set(['bmp','png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()+'/upload_picture'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>Photo Upload</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=upload>
    </form>
    '''


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():

    message = "null"
    predictedTypeRate = 0.0
    tags = []
    result = -1
    maxConfidence = 0.0

    #下面那几个变量只是为了写入信息，不需要时应该删掉
    writeName = "未命名"
    typeList = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    writePredictRate = []
    writeTotalRate = {}

    try:

        if request.method == 'POST':
            file = request.files['file']
            # print(request.values.get("tags"))
            if file and allowed_file(file.filename):
                # filename = secure_filename(file.filename)
                fileTime = time.strftime("%Y-%m-%d", time.localtime())+"-"+time.strftime("%H:%M:%S", time.localtime())
                try:
                    name = secure_filename(file.filename)
                    suffix = name[name.rfind("."):]
                    if request.values.get("name")!="null":
                        filename = request.values.get("name")+fileTime+suffix
                        writeName = request.values.get("name")
                    else:
                        filename = secure_filename(file.filename)
                        writeName = filename
                except:
                    filename = secure_filename(file.filename)
                    writeName = filename

                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                file_url = url_for('uploaded_file', filename=filename)

                try:
                    tagsString = request.values.get("tags")
                    # print(tagsString)
                    if tagsString!="":
                        tags = tagsString.split(",")
                except:
                    tagsString = ""
                    pass

                try:

                    rate = runModel2.getResult(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    rate = rate.tolist()#转为list，方便处理
                    writePredictRate =rate
                    # print(rate)
                    predictedTypeRate = max(rate)#留一手，若无tags传过来，这两个就用上了
                    maxConfidence = predictedTypeRate#看看纯预测的置信度最高的是多少
                    result = rate.index(predictedTypeRate)


                    if len(tags)!=0:
                        weight2Dict = {}

                        for i in range(0,len(rate)):
                            weight2Dict[i] = 0.4*rate[i]
                        for tag in tags:
                            # print(tags)
                            weight2Dict[int(type2Dict[tag])-1] += weights2Dict[tag]*0.6
                            typeList[int(type2Dict[tag])-1] += weights2Dict[tag]
                            if tag=="身体水肿":#因为有重叠的，还要算上另一个
                                weight2Dict[6] += weights2Dict["水肿"]*0.6
                            if tag=="大便稀溏":
                                weight2Dict[3] += weights2Dict["大便稀"]*0.6
                            if tag=="胸胁疼痛":
                                weight2Dict[2] += 0.3*0.6
                            if tag=="乏力":
                                weight2Dict[1] += 0.5*0.6

                        writeTotalRate = weight2Dict
                        typeWeight = sorted(weight2Dict.items(),key=lambda item:item[1])

                        result = typeWeight[-1][0]#预测体质名称下标
                        predictedTypeRate = typeWeight[-1][1]#置信度
                        # print(predictedTypeRate)

                    else:
                        writeTotalRate = writePredictRate

                    # type = value2Dict[str(result+1)]
                    # # print(type)

                    # newname = filename[:filename.find(".")] + "," + tagsString +","+ type +filename[filename.find("."):]

                    # os.chdir(os.getcwd()+'/upload_picture')

                    # os.rename(filename,newname)
                except:
                    message = "服务器异常1,请过几分钟再试!若仍不行,请联系1348040397@qq.com"
                    pass

        else:
            message = "请求方式错误!正确请求为POST"
            return html

    except:
        message = "服务器异常2,请过几分钟再试!若仍不行,请联系1348040397@qq.com"

    # num = str(random.randint(0,9))

    # print(predictedTypeRate)
    # print(maxConfidence)

    if len(tags)!=0 and predictedTypeRate>0.25:
        num = str(result+1)
    elif len(tags)==0 and predictedTypeRate>0.50:
        num = str(result+1)
    # elif maxConfidence<0.40:
    #     num = str(0)
    else:
        num = str(1)
    
    t = {'message':message,'confidence':str( round(predictedTypeRate, 3) ) ,'body':value2Dict[num],'imgUrl':imgUrl[value2Dict[num]],'year_month_day':time.strftime("%Y-%m-%d", time.localtime()),'time':time.strftime("%H:%M", time.localtime())  }
    
    path  = "information.csv"

    with open(path,'a+',newline=None,encoding='gbk') as f:
        csv_write = csv.writer(f)
        writeTime = time.strftime("%Y-%m-%d", time.localtime())+"-"+time.strftime("%H:%M", time.localtime())
        data_row = [writeName,filename,writeTime,tagsString,typeList,writePredictRate,writeTotalRate,value2Dict[num]]
        csv_write.writerow(data_row)

    # t = {'body':value2Dict['0'],'imgUrl':imgUrl[value2Dict['0']],'year_month_day':time.strftime("%Y-%m-%d", time.localtime()),'time':time.strftime("%H:%M", time.localtime())  }
    return jsonify(t)


if __name__ == '__main__':
   # app.run(host='0.0.0.0')
    app.run(host='0.0.0.0',ssl_context=('3597134_www.aitongue.tech.pem', '3597134_www.aitongue.tech.key'))
