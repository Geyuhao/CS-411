var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var bodyParser = require('body-parser');
var flash = require('express-flash');
var session = require('express-session');
var db=require('./database');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

var visit_count = 0;
var comment_count = 0;
 
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
 
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
 
// app.use('/', indexRouter);
app.use('/users', usersRouter);

app.use(session({ 
    secret: '123456catr',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
}))
 
app.use(flash());
 
/* GET home page. */
app.get('/', function(req, res, next) {
  console.log('Someone visit your web !');
  res.render('index', { title: 'main page' });
  visit_count += 1;
  console.log('# visit is',visit_count,'# comment is',comment_count);
});
 
app.post('/user', function(req, res, next) {
  var f_name = req.body.f_name;
  var l_name = req.body.l_name;
  var email = req.body.email;
  var message = req.body.message;
 
  comment_count += 1;

  var sql = `INSERT INTO contacts (f_name, l_name, email, message, created_at) VALUES ("${f_name}", "${l_name}", "${email}", "${message}", NOW())`;
  db.query(sql, function(err, result) {
    if (err) throw err;
    console.log('record inserted');
    req.flash('success', 'Data added successfully!');
    res.redirect('/');
  });
});
 
// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});
 
// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};
 
  // render the error page
  res.status(err.status || 500);
  res.render('error');
});
 
// port must be set to 3000 because incoming http requests are routed from port 80 to port 8080
// app.listen(3000, function () {
//     console.log('Node app is running on port 3000');
// });
 
module.exports = app;