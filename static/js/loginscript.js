var form = document.querySelector('.login_form');

form.addEventListener('submit', function (event) {
  event.preventDefault();
  var form = document.querySelector('.login_form');
  var submitBtn = form.querySelector('.sumbitBtn');
  var email = form.querySelector('.user_email');
  var password = form.querySelector('.user_password');
  var errors = form.querySelectorAll('.error')

  for (var i = 0; i < errors.length; i++) {
    errors[i].remove()
  }
  //console.log('clicked on validate');
  //alert(name.value);
  validateEmail(email);
  validatePassword(password);
  var errors = form.querySelectorAll('.error')
  if (errors.length==0) alert("Logged in");
})

function validateEmail(email) {
  if (!email.value) 
  {
    //alert("Username chould not be empty");
    var error = generateError('Email chould not be empty');
    email.parentElement.insertBefore(error, email);
  }
}

function validatePassword(password) {
  if (!password.value) 
  {
    //alert("Username chould not be empty");
    var error = generateError('Password chould not be empty');
    password.parentElement.insertBefore(error, password);
  }
}

var generateError = function (text) {
  var error = document.createElement('div');
  error.className = 'error';
  error.style.color = 'red';
  error.innerHTML = text;
  return error;
}
