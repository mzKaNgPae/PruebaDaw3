var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/styles.css',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(

      fetch(event.request)
      .then((result)=>{
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })
        
      })
      .catch(function(e){
          return caches.match(event.request)
      })
  

     
    );
});


//NOTIFICACIONES PUSH

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
    apiKey: "AIzaSyAVfHgLuS0Pkw6fVbmPPiK7EjXEXnTSTIo",
    authDomain: "cardetail-93e21.firebaseapp.com",
    projectId: "cardetail-93e21",
    storageBucket: "cardetail-93e21.appspot.com",
    messagingSenderId: "616039439604",
    appId: "1:616039439604:web:05813817d72b7cefe2d2a1"
  };
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){
    let title = 'titulo de la notificacion'

      let options = {
        body: 'este es el mensaje',
        icon: '/static/adm/img/cardetail-blanco.png'
      }

      self.registration.showNotification(title,options)
})
