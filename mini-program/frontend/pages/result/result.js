// pages/result/result.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    //图片存储链接
    bodyIntroduce:"人体阳气化生不足，温煦作用下降生里寒。",
    userInfo: {},
    hasUserInfo: false, 
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    canIUseGetUserProfile: false,
    canIUseOpenData: wx.canIUse('open-data.type.userAvatarUrl') && wx.canIUse('open-data.type.userNickName'), // 如需尝试获取用户信息可改为false
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
//     const data = JSON.parse(options.data);
//     console.log(data);
//     //console.log(options)
//  //this.setData({image:options.file});
//  if(data.message!="null")
//     wx.showModal({
//       title: '提示',
//       content:data.message,
//       complete(res) {
//         wx.navigateBack();
//       }
//     })

//    this.setData({resultUrl:data.imgUrl,  
//    display:'block'//展示蒙版       
//    });
//    var obj={
//      body:data.body,
//      year_month_day:data.year_month_day,
//      time:data.time
//    }
//     const temp = wx.getStorageSync('log') || [];
//    temp.unshift(obj);
//     wx.setStorageSync('log', temp);


//------------------------------------------------！
if (wx.getUserProfile) {
  this.setData({
    canIUseGetUserProfile: true
  })
}
  },
  getUserProfile(e) {
    // 推荐使用wx.getUserProfile获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认，开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
    wx.getUserProfile({
      desc: '展示用户信息', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
      success: (res) => {
        console.log(res)
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    })
    
console.log(this.data.userInfo)
  
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

  },


hideview: function() {
  this.setData({
    display: "none"
  })
},
  clickDrinks:function(){
    wx.navigateTo({
      url: '/pages/drinks/drinks',
    })
  },
  clickDetail:function(){
    wx.navigateTo({
      url: '/pages/detail/detail',
    })
  }
})
