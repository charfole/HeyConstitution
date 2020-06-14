//var app = getApp()
Page({
  
  /**
   * 页面的初始数据
   */
  data: {
    scanitem:['','','']
  },
clickHelp: function(){
 wx.navigateTo({
   url: '../help/help',
 })
},
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
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

    return {

      title: '草木多闻',
      desc: '快来体验舌诊识别体质吧!',
      path: '/pages/index/index'

    }

  },
  
  
  clickToTake: function()
  {
    wx.navigateTo({
      url: '/pages/optional/optional',
    })
  },
  clickLogs: function () {
    wx.navigateTo({
      url: '/pages/logs/logs',
    })
  },
  clickDrinks: function () {
      wx.navigateTo({
        url: '/pages/drinks/drinks',
      })
  }
})
