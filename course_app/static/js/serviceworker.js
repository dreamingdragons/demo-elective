// var cacheName = 'hello-pwa';
// var filesToCache = [
//   '.',
//   '/failed/'
// ];

// /* Start the service worker and cache all of the app's content */
// self.addEventListener('install', function(e) {
//   e.waitUntil(
//     caches.open(cacheName)
//     .then(function(cache) {
//       return cache.addAll(filesToCache);
//     })
//   );
// });

// /* Serve cached content when offline */
// self.addEventListener('fetch', function(e) {
//   e.respondWith(
//     caches.match(e.request).then(function(response) {
//       return response || fetch(e.request);
//     })
//   );
// });




// var CACHE_NAME = 'static-cache';
// var urlsToCache = [
//   '.',
//   '/failed/'
// ];
// self.addEventListener('install', function(event) {
//   event.waitUntil(
//     caches.open(CACHE_NAME)
//     .then(function(cache) {
//       return cache.addAll(urlsToCache);
//     })
//   );
// });

// self.addEventListener('fetch', function(event) {
//   event.respondWith(
//     caches.match(event.request)
//     .then(function(response) {
//       return response || fetchAndCache(event.request);
//     })
//   );
// });

// function fetchAndCache(url) {
//   return fetch(url)
//   .then(function(response) {
//     // Check if we received a valid response
//     if (!response.ok) {
//       throw Error(response.statusText);
//     }
//     return caches.open(CACHE_NAME)
//     .then(function(cache) {
//       cache.put(url, response.clone());
//       return response;
//     });
//   })
//   .catch(function(error) {
//     console.log('Request failed:', error);
//     return catches.match('/failed/');
//   });
// }



var cacheVersion = 1;
var currentCache = {
  offline: 'offline-cache' + cacheVersion
};
const offlineUrl = '/offline/';

this.addEventListener('install', event => {
  event.waitUntil(
    caches.open(currentCache.offline).then(function(cache) {
      return cache.addAll([
          offlineUrl
      ]);
    })
  );
});

this.addEventListener('fetch', event => {
  // request.mode = navigate isn't supported in all browsers
  // so include a check for Accept: text/html header.
  if (event.request.mode === 'navigate' || (event.request.method === 'GET' && event.request.headers.get('accept').includes('text/html'))) {
        event.respondWith(
          fetch(event.request.url).catch(error => {
              // Return the offline page
              return caches.match(offlineUrl);
          })
    );
  }
  else{
        // Respond with everything else if we can
        event.respondWith(caches.match(event.request)
                        .then(function (response) {
                        return response || fetch(event.request);
                    })
            );
      }
});