function changeLang(lang)
  {
if(typeof(Storage)!=="undefined") {
  
  if (lang == 'eng')
  {
  localStorage.language="English";
  //return "home";
  //window.location.reload();
   //window.location = {% templates 'index.html' %}
    alert(window.location.href);
  }
  else if (lang == 'ru')
  {
  localStorage.language="Russian";
  //window.location.href = "/templates/rus.html";
  //window.location.reload();
  }
  }
}


window.onload = function() {
if(!localStorage.getItem('firstLoad')) {
if (localStorage.language=="English" )
  {
   localStorage['firstLoad'] = true;
   //window.location.href = "index.html";
   //window.location.reload();
  }
else if (localStorage.language=="Russian")
  {
  localStorage['firstLoad'] = true;
  //window.location.href = "../templates/rus.html";
  //window.location.reload();
  }
}
  else
      localStorage.removeItem('firstLoad');
}

