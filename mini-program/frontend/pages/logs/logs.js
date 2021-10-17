//logs.js
const util = require('../../utils/util.js')
Page({
  data: {
    log: [],
    hasLog:false,
  },
  // onLoad: function () {
  //   this.setData({
  //     logs: (wx.getStorageSync('logs') || []).map(log => {
  //       return util.formatTime(new Date(log))
  //     })
  //   })
  // }
    onLoad: function () {
      console.log(wx.getStorageSync('log'))
    this.setData({
      log: wx.getStorageSync('log') || []
      })
      if(this.data.log.length!=0)
      {
        this.setData({
          hasLog:true 
          })
      }
    
  },

  clearStorage:function()
  {
    var that=this;
    wx.showModal({
      title: '清空所有记录',
      content: '您确定要清空所有记录吗？',
      success(res){
        if(res.confirm)
          wx.clearStorageSync();
        that.setData({
          log: wx.getStorageSync('log') || []
        })
      }
    })
  }
})
