// pages/optional/optional.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    list: [
     { name: '乏力', checked: false }, 
     { name: '口渴', checked: false },
      { name: '痰多', checked: false },
     { name: '自汗', checked: false },
      { name: '心烦', checked: false },
      { name: '失眠', checked: false },
      { name: '口苦', checked: false },
      { name: '易长痘痘', checked: false },
      { name: '身体困重', checked: false },
      { name: '耐受寒热', checked: false },
      { name: '不易疲劳', checked: false },
      { name: '自觉发热', checked: false },
      { name: '多愁善感', checked: false },
     { name: '口腔溃疡', checked: false },
    { name: '头胀胸闷', checked: false },
   { name: '面色晦暗', checked: false },
   { name: '胸胁疼痛', checked: false },
      { name: '少气懒言', checked: false },
      { name: '容易生气', checked: false },
      { name: '容易感冒', checked: false },
      { name: '畏寒肢冷', checked: false },
      { name: '嗳气叹气', checked: false },
      { name: '大便稀溏', checked: false },
      { name: '消化不良', checked: false },
      { name: '关节疼痛', checked: false },
      { name: '皮肤干燥', checked: false },
      { name: '皮肤粗糙有瘀斑', checked: false },
      { name: '月经血块', checked: false },
      { name: '身体水肿', checked: false },



     ],
    max_selected: 4,
    cur_selected: 0,
    arr_selected: [],
    name:null
  },




  lable_click: function (e) {
    var that = this;
    console.log(e.currentTarget.dataset);
    var index = e.currentTarget.dataset.index;
    var checked = e.currentTarget.dataset.checked;
    var name = e.currentTarget.dataset.name;
    //判断是否达到可选上限
    console.log(checked)
    if (!checked) {
      if (that.data.cur_selected >= that.data.max_selected) {
        //弹出模态框
        wx.showModal({
          content: '为了使结果更准确，最多选择'+that.data.max_selected+'项主要症状',
          showCancel: false
        })
        return;
      }
      that.data.cur_selected++;
      var temp = "list[" + index + "].checked";
      that.setData({ [temp]: !checked });
      that.data.arr_selected.push(name);
      console.log("插入后" + that.data.arr_selected)
    }
    //取消选中
    else {
      var temp = "list[" + index + "].checked";
      that.setData({ [temp]: !checked })
      for (var i in that.data.arr_selected)
        if (that.data.arr_selected[i] == name)
          that.data.arr_selected.splice(i, 1);
      that.data.cur_selected--;
      console.log("取消后" + that.data.arr_selected);
    }


  },
  
  submit:function(){
    var that=this;
    wx.redirectTo({
      url: "../crop/crop?data=" + that.data.arr_selected,
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },

checkbox_group_change:function(e){
  console.log(e.detail.value)
  
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
})