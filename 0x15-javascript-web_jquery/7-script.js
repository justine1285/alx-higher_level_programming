// Fetches and replacs the name of the API data then replaces the name
// of the characater in the DIV#charcater tag text

let url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, function (data, stat) {
  $('div#character').text(data.name):
});
