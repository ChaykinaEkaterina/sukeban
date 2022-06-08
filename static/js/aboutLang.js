
function changeLang(lang)
  {
if(typeof(Storage)!=="undefined") {
  
  if (lang == 'eng')
  {
  localStorage.clear();
  localStorage.language="English";
  //localStorage.setItem('langChanged', true);
  window.location.href = "about.html";
  //window.location.reload();
  }
  else if (lang == 'ru')
  {
  localStorage.clear();
  localStorage.language="Russian";
  //localStorage.setItem('langChanged', true);
  window.location.href = "aboutrus.html";
  //window.location.reload();
  }
  }
}



window.onload = function() {
if(!localStorage.getItem('firstLoad')) {
if (localStorage.language=="English" )
  {
   localStorage['firstLoad'] = true;
   //window.location.href = "about.html";
   //window.location.reload();
  }
else if (localStorage.language=="Russian")
  {
  localStorage['firstLoad'] = true;
  window.location.href = "aboutrus.html";
  //window.location.reload();
  }
}
  else
      localStorage.removeItem('firstLoad');
}

