var User = {
  count: 1,

  getCount: function() {
    return this.countn;
  }.bind(User)
};

 console.log(User.getCount());

    var func = User.getCount;
    console.log(func());
