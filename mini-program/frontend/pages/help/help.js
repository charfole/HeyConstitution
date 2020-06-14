// pages/help/help.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    showIndex:1,
  },
  acTap: function (e) {
    if (e.currentTarget.dataset.index != this.data.showIndex) {
      this.setData({
        showIndex: e.currentTarget.dataset.index
      })
    } else {
      this.setData({
        showIndex:0
      })
    }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({showIndex:1})
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

 
    name: "tuiCollapse",
    props: {
      //collapse背景颜色
      bgColor: {
        type: String,
        default: 'none'
      },
      //collapse-head 背景颜色
      hdBgColor: {
        type: String,
        default: '#fff'
      },
      //collapse-body 背景颜色
      bdBgColor: {
        type: String,
        default: 'none'
      },
      //collapse-body实际高度 open时使用
      height: {
        type: String,
        default: 'auto'
      },
      //close时translateY ，当bd高度固定时，建议值为0
      translateY: {
        type: String,
        default: '-50%'
      },
      //索引
      index: {
        type: Number,
        default: 0
      },
      //当前索引，index==current时展开
      current: {
        type: Number,
        default: -1
      },
      // 是否禁用
      disabled: {
        type: [Boolean, String],
        default: false
      },
      //是否带箭头
      arrow: {
        type: [Boolean, String],
        default: true
      },
      //箭头颜色
      arrowColor: {
        type: String,
        default: "#333"
      }
    },
    watch: {
      current() {
        this.updateCurrentChange()
      }
    },
    created() {
      this.updateCurrentChange()
    },
    data() {
      return {
        isOpen: false
      };
    },
    methods: {
      updateCurrentChange() {
        this.isOpen = this.index == this.current
      },
      handleClick() {
        if (this.disabled) return;
        this.$emit("click", {
          index: Number(this.index)
        })
      }
    }


})

  
 
 