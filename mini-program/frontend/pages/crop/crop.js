// pages/crop/crop.js
const app=getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    src: '',
    width: 250,//宽度
    height: 250,//高度
    uploadData:[],
    tags:null,
    name:null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options.data)
    //获取到image-cropper实例
    var that=this;
    that.data.uploadData.push(options.data);
    that.data.tags=that.data.uploadData.join(",");
    that.data.name=options.name
    this.cropper = this.selectComponent("#image-cropper");
    //开始裁剪
    wx.chooseImage({
      success(res) {
        const tempFilePaths = res.tempFilePaths
        //console.log(tempFilePaths);
        that.cropper.pushImg(tempFilePaths);
        app.globalData.imgSrc=tempFilePaths;
     
      }
    })
    
  },
  // cropperload(e) {
  //   console.log("cropper初始化完成");
  // },
  loadimage(e) {
    console.log("图片加载完成", e.detail);
 
    //重置图片角度、缩放、位置
    this.cropper.imgReset();
  },
  submit() {
    var that=this;

    this.cropper.getImg((obj) => {
      console.log(obj)
       wx.showLoading({
      title: '识别中，请稍等',
      mask: true
    })
    console.log(that.data.tags);
      console.log(typeof (that.data.tags));
      wx.uploadFile({
        
        url: 'http://8.129.131.241:8777/', //仅为示例，非真实的接口地址
        filePath: obj.url,
        name: 'file',
        formData:
        {
          'tags': that.data.tags
        },
        timeout:12000,
        success(res) {
        
         
console.log(res.data)
          //const resor =res;
          //const data=res.data;
          //console.log(data);
        
          //console.log(resor);
          wx.hideLoading();
          app.globalData.options=res.data
          wx.switchTab({
           
            //url: "../result/result?val=" + data + "&file=" + app.imgSrc
            url: "../result/result"
          })
     
       
         
        },
        fail(){
          console.log("超时");
          wx.hideLoading();
          wx.showModal({
            title: '连接错误',
            content: '网络超时，请稍后重试!',
            showCancel:false,
            complete(res) {
              wx.navigateBack();
            }
          })
        },
      })
    });
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})