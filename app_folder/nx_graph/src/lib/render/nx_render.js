import * as d3 from "d3";

const dims = {
  width: 758,
  height: 458,
}
export default class nxWidget {

  constructor(el, data, onClick) {

    const self = this;

    self.el = el;

    self.data = data;

    self.onClick = onClick;

    setTimeout(() => {
      self.setCanvas();
      self.drawGraph(self.data);
    }, 148);
  }

  setCanvas() {
      const self = this;

      self.svg = d3.select(self.el)
              .append("svg")
              .attr("id", "svg_nx")
              .attr("width", "100%")
              .attr("height", dims.height);

      self.container = self.svg.append("g");

      self.linkGroup = self.container
                .append("g")
                .attr("class", "links");

      self.nodeGroup = self.container
                .append("g")
                .attr("class", "nodes");

      self.labelNodeGroup = self.container
                .append("g")
                .attr("class", "labelNodes");

    }


    drawGraph(data) {

      const self = this;
      self.data = data;
      self.svg = d3.select(self.el).select("#svg_nx");
      self.linkGroup = self.svg.select(".links");
      self.nodeGroup = self.svg.select(".nodes");
      self.labelNodeGroup = self.svg.select(".labelNodes");
      console.log(self.data);
      var color = d3.scaleOrdinal(d3.schemeCategory10);
      self.label = {
          'nodes': [],
          'links': []
      };

      self.data.nodes.forEach(function(d, i) {
          self.label.nodes.push({node: d});
          self.label.nodes.push({node: d});
          self.label.links.push({
              source: i * 2,
              target: i * 2 + 1
          });
      });

      self.wScale = d3.scaleLinear()
                        .domain([
                          d3.min(self.data.links, d => d["value"]),
                          d3.max(self.data.links, d => d["value"])
                        ])
                        .range([1, 9]);

      self.link = self.linkGroup
          .selectAll("line")
          .data(self.data.links)
          .join("line")
          .attr("stroke", "#aaa")
          .attr("stroke-width", d => self.wScale(d["value"]));

      self.node = self.nodeGroup
          .selectAll("circle")
          .data(self.data.nodes)
          .join("circle")
          .attr("r", 9)
          .attr("fill", "lightblue")
          .on("click", function(event, d) {
            self.onClick(d);
          })

      self.labelNode = self.labelNodeGroup
          .selectAll("text")
          .data(self.label.nodes)
          .join("text")
          .text(function(d, i) { return i % 2 == 0 ? "" : d.node.id; })
          .style("fill", "#555")
          .style("font-family", "Arial")
          .style("font-size", 12)
          .style("pointer-events", "none"); // to prevent mouseover/drag capture

      self.labelLayout = d3.forceSimulation(self.label.nodes)
          .force("charge", d3.forceManyBody().strength(-50))
          .force("link", d3.forceLink(self.label.links).distance(0).strength(2));

      self.graphLayout = d3.forceSimulation(self.data.nodes)
          .force("charge", d3.forceManyBody().strength(-3000))
          .force("center", d3.forceCenter(dims.width / 2, dims.height / 2))
          .force("x", d3.forceX(dims.width / 2).strength(1))
          .force("y", d3.forceY(dims.height / 2).strength(1))
          .force("link", d3.forceLink(self.data.links).id(function(d) {return d.id; }).distance(50).strength(1))
          .on("tick", ticked);

      self.adjlist = [];

      self.data.links.forEach(function(d) {
          self.adjlist[d.source.index + "-" + d.target.index] = true;
          self.adjlist[d.target.index + "-" + d.source.index] = true;
      });

      self.neigh = function(a, b) {
          return a == b || self.adjlist[a + "-" + b];
      }


      self.svg.call(
          d3.zoom()
              .scaleExtent([.1, 4])
              .on("zoom", function(event) { self.container.attr("transform", event.transform); })
      );


      self.node.on("mouseover", focus).on("mouseout", unfocus);

      self.node.call(
          d3.drag()
              .on("start", dragstarted)
              .on("drag", dragged)
              .on("end", dragended)
      );

      self.node.on("mouseover", focus).on("mouseout", unfocus);

      function ticked() {

        self.node.call(updateNode);
        self.link.call(updateLink);

        self.labelLayout.alphaTarget(0.3).restart();

        self.labelNode.each(function(d, i) {
            if(i % 2 == 0) {
                d.x = d.node.x;
                d.y = d.node.y;
            } else {
                var b = this.getBBox();
                // b.width = dims.width;
                var diffX = d.x - d.node.x;
                var diffY = d.y - d.node.y;

                var dist = 2*Math.sqrt(diffX * diffX + diffY * diffY);

                var shiftX = b.width * (diffX - dist) / (dist * 2);
                shiftX = Math.max(-b.width, Math.min(0, shiftX));
                var shiftY = -9.9; 
                this.setAttribute("transform", "translate(" + (d.x + shiftX) + "," + (d.y + shiftY) + ")");
            }
        });
        self.labelNode.call(updateNode);

      }
        function fixna(x) {
            if (isFinite(x)) return x;
            return 0;
        }

        function focus(event, d) {
            var index = d3.select(event.target).datum().index;
            self.node.style("opacity", function(o) {
                return self.neigh(index, o.index) ? 1 : 0.1;
            });
            self.labelNode.attr("display", function(o) {
              return self.neigh(index, o.node.index) ? "block": "none";
            });
            self.link.style("opacity", function(o) {
                return o.source.index == index || o.target.index == index ? 1 : 0.1;
            });
        }

        function unfocus() {
           self.labelNode.attr("display", "block");
           self.node.style("opacity", 1);
           self.link.style("opacity", 1);
        }

        function updateLink(link) {
            self.link.attr("x1", function(d) { return fixna(d.source.x); })
                .attr("y1", function(d) { return fixna(d.source.y); })
                .attr("x2", function(d) { return fixna(d.target.x); })
                .attr("y2", function(d) { return fixna(d.target.y); });
        }

        function updateNode(node) {
            self.node.attr("transform", function(d) {
                return "translate(" + fixna(d.x) + "," + fixna(d.y) + ")";
            });
        }

        function dragstarted(event, d) {
            event.sourceEvent.stopPropagation();
            if (!event.active) self.graphLayout.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }

        function dragged(event, d) {
            d.fx = event.x;
            d.fy = event.y;
        }

        function dragended(event, d) {
            if (!event.active) self.graphLayout.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }

    }
}
