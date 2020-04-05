google.charts.load('current', {
  'packages':['geochart'],
  'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
});

google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {
  var data = google.visualization.arrayToDataTable([
    ['Country', 'Popularity'],
    ['Ethiopia', 2000],
    ['Egypt', 300],
    ['Kenya', 400],
    ['Sudan', 500],
    ['Lesotho', 600],
    ['Ghana', 700]
  ]);

  var dataAdded = google.visualization.arrayToDataTable([
         ['City',   'Population', 'Area'],
         ['Rome',      2761477,    1285.31],
         ['Milan',     1324110,    181.76],
         ['Naples',    959574,     117.27],
         ['Turin',     907563,     130.17],
         ['Palermo',   655875,     158.9],
         ['Genoa',     607906,     243.60],
         ['Bologna',   380181,     140.7],
         ['Florence',  371282,     102.41],
         ['Fiumicino', 67370,      213.44],
         ['Anzio',     52192,      43.43],
         ['Ciampino',  38262,      11]
       ]);

  var options = {
                  region: '002'
                  };
  var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));
  chart.draw(data, options);

  var markers_options = {
                  region: 'ETH',
                  displayMode: 'markers',
                  colorAxis: {colors: ['green', 'blue']}
                  };
  var markers_chart = new google.visualization.GeoChart(document.getElementById('chart_div'));
  markers_chart.draw(dataAdded, markers_options);

}
