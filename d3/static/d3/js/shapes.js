function render_shapes() {

  var svgContainer = d3.select("#shapes_circles").append("svg").attr("width", 300).attr("height", 200);

  d3.json('/d3/shapes-data/', function(error, data) {
    var circles = svgContainer.selectAll("circle").data(data).enter().append("circle");
    var circleAttributes = circles
      .attr("cx", function (d) { return d.x_axis; })
      .attr("cy", function (d) { return d.y_axis; })
      .attr("r", function (d) { return d.radius; })
      .attr("fill", function (d) { return d.color; });
  });
}


// NOTE:
$(function() {
    render_shapes();
});
