// pages/drinks.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    drinks: { 
      '平和质': [
        { '名字': '百莲耳汤', '功效': '健脾养心安神', '成分': '莲子10克、百合10克、银耳10克', '状态': '热(推荐)', '热量': '500卡路里' }, 
        { '名字': '红米粥', '功效': '健脾祛湿', '成分': '红豆10克、薏米30克、梗米20克', '状态': '热(推荐)', '热量': '500卡路里' },
        { '名字': '胡萝卜山药汤', '功效': '健护脾胃，益气养阴', '成分': '鲜淮山1斤、猪尾骨1块、胡萝卜1根', '状态': '热(推荐)', '热量': '500卡路里' }
        ],
    '气虚质': [
      { '名字': '花胶党参鸡汤', '功效': '健脾养胃，益气补血', '成分': '花胶干品20克、党参20克、生姜3片，鸡半只(2人份)', '状态': '热(推荐)', '热量': '500卡路里' },
      { '名字': '参山莲枣汤', '功效': '健脾养胃，养心安神', '成分': '党参10克、山药10克、大枣10克、莲子10克', '状态': '热(推荐)', '热量': '500卡路里'},
      { '名字': '猴头菇鸡汤汤', '功效': '健脾养胃，益气养阴', '成分': '猴头菇1包、鸡半只、红枣5-6颗、枸杞1-2把、人参3片、米酒半杯', '状态': '热(推荐)', '热量': '500卡路里'}
    ],
    '气郁质':[
 { '名字': '佛手猪肝汤', '功效': '调和脾胃，疏肝解郁', '成分': '佛手片10克、鲜猪肝150克、麦片10克、盐、葱适量', '状态': '热(推荐)', '热量': '500卡路里' },
      { '名字': '陈皮玫瑰汤', '功效': '健脾疏肝解郁', '成分': '玫瑰10克、陈皮10克', '状态': '热(推荐)', '热量': '500卡路里'},
      { '名字': '百芎汤', '功效': '养阴安神，活血疏肝', '成分': '川芎10克、百合10克、龙眼肉10克', '状态': '热(推荐)', '热量': '500卡路里'}
    ],
    '湿热质': [
      { '名字': '绿豆海带煲排骨汤', '功效': '清热解毒，行气利湿', '成分': '猪排骨400克、绿豆50克、鲜海带100克、生姜3~5片，陈皮1瓣', '状态': '热(推荐)', '热量': '500卡路里' },
      { '名字': '胡萝卜茅根马蹄猪骨汤', '功效': '清热祛湿，生津止渴，利尿', '成分': '猪骨500克、茅根50克、马蹄6个、胡萝卜半个、蜜枣2粒', '状态': '热(推荐)', '热量': '500卡路里'},
      { '名字': '地石汤', '功效': '祛湿化痰、健脾补肺', '成分': '生地10克、石斛10克', '状态': '热(推荐)', '热量': '500卡路里'}
    ],
      '痰湿质': [
        { '名字': '冬瓜薏米猪骨汤', '功效': '健脾祛湿，利尿消肿', '成分': '猪骨500克、冬瓜700克、薏米100克、甜玉米1根、生姜1块', '状态': '热(推荐)', '热量': '500卡路里' },
        { '名字': '地石汤', '功效': '祛湿化痰、健脾补肺', '成分': '生地10克、石斛10克', '状态': '热(推荐)', '热量': '500卡路里'},
        { '名字': '杏仁薏米汤', '功效': '祛湿化痰、健脾补肺', '成分': '杏仁10克、薏米10克', '状态': '热(推荐)', '热量': '500卡路里'}
      ],
      '血瘀质': [
        { '名字': '田七排骨鸡脚汤', '功效': '活血化瘀，消肿止痛', '成分': '鸡脚数只、排骨500克、田七20克、姜1片、苹果半只', '状态': '热(推荐)', '热量': '500卡路里' },
        { '名字': '归母汤', '功效': '活血祛瘀，调经止痛', '成分': '当归10克、益母草10克、山楂10克', '状态': '热(推荐)', '热量': '500卡路里'},
        { '名字': '桃红汤', '功效': '活血调经、润肠通便', '成分': '桃仁10克、红花10克、大枣10克', '状态': '热(推荐)', '热量': '500卡路里'}
      ],
      '阳虚质': [{ '名字': '参归姜枣汤', '功效': '清热解毒，利气行湿', '成分': '党参10克、当归10克、生姜6克、大枣10克', '状态': '热(推荐)', '热量': '500卡路里' },
        { '名字': '巴戟炖猪肚汤', '功效': '强筋骨、安五脏、补中气、温肾阳', '成分': '巴戟50克、猪肚350克、姜10克、胡椒粒5克、调味料适量', '状态': '热(推荐)', '热量': '500卡路里'},
        { '名字': '苁蓉汤', '功效': '温补肾阳、固精缩尿', '成分': '肉苁蓉10克、菟丝子10克、大枣10克', '状态': '热(推荐)', '热量': '500卡路里'}
      ],
      '阴虚质': [
        { '名字': '杞冬参汤', '功效': '养阴益气，生津止渴', '成分': '枸杞10克、麦冬10克、西洋参10克', '状态': '热(推荐)', '热量': '500卡路里' },
        { '名字': '麦冬淮山玉竹煲鸽汤', '功效': '养阴润肺、健脾和胃', '成分': '鸽子1只、淮山15克、玉竹15克、麦冬15克、姜1片', '状态': '热(推荐)', '热量': '500卡路里'},
        { '名字': '杏仁汤', '功效': '养阴润肺，通肠润便', '成分': '杏仁10克、芝麻5克', '状态': '热(推荐)', '热量': '500卡路里'}
      ],
    },
  body:null,
  name:null,
  use:null,
  form:null,
  tem:null,
  energy:null,
  showIndex:0,
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) 
  {
    const item=wx.getStorageSync('log') || []
  if(item.length!=0){
    const body = item[0].body
    this.setData({
      body:body,
      name:this.data.drinks[body][0]['名字'],
      use: this.data.drinks[body][0]['功效'],
      form: this.data.drinks[body][0]['成分'],
      tem: this.data.drinks[body][0]['状态'],
      energy: this.data.drinks[body][0]['热量']
    })
  }
  else{
    wx.showModal({
      title: '提示',
      content: '检测到您还未诊断体质，请现在开始吧!',
      complete(res) {
        wx.navigateBack();
      }
    })
  }
  },
  change: function (e) {
    if (e.currentTarget.dataset.index != this.data.showIndex) {
      this.setData({
        showIndex: e.currentTarget.dataset.index
      })
    }
    //console.log(this.data.showIndex)
    const body=this.data.body
    const index=this.data.showIndex
    //console.log(body)
    this.setData({
      name: this.data.drinks[body][index]['名字'],
      use: this.data.drinks[body][index]['功效'],
      form: this.data.drinks[body][index]['成分'],
      tem: this.data.drinks[body][index]['状态'],
      energy: this.data.drinks[body][index]['热量']
    })
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