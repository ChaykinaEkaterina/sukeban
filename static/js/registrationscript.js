var form = document.querySelector('.register_form');

form.addEventListener('submit', function (event) {
  event.preventDefault();
  var form = document.querySelector('.register_form');
  var submitBtn = form.querySelector('.sumbitBtn');
  var name = document.querySelector('.user_name');
  var email = form.querySelector('.user_email');
  var password = form.querySelector('.user_password');
  var errors = form.querySelectorAll('.error')

  for (var i = 0; i < errors.length; i++) {
    errors[i].remove()
  }
  //console.log('clicked on validate');
  //alert(name.value);
  validateName(name);
  validateEmail(email);
  validatePassword(password);
  var errors = form.querySelectorAll('.error')
  if (errors.length==0) alert("Registration completed");
})

function validateName(name) {
  var onlyLetters = /^[a-zA-Z]*$/.test(name.value);
  
  if (!name.value) 
  {
    var error = generateError('Username chould not be empty');
    name.parentElement.insertBefore(error, name);
  }
  else if (!onlyLetters) 
  {
    var error = generateError('Username should consist only of letters');
    name.parentElement.insertBefore(error, name);
  }
  else 
  {
    if (name.value.charAt(0)!=name.value.charAt(0).toUpperCase())
    {
    var error = generateError('First letter must be uppercase');
    name.parentElement.insertBefore(error, name);
    }
  }
}

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
