import { useEffect, useState } from "react";

import ForceGraph2D from "react-force-graph-2d";

import { getGraph } from "../services/api";


function IntelligenceGraph() {

  const [graph, setGraph] = useState({
    nodes: [],
    links: [],
  });


  useEffect(() => {

    getGraph()
      .then(setGraph)
      .catch(console.error);

  }, []);


  return (
    <div className="intelligence-graph">

      <ForceGraph2D
        graphData={graph}

        backgroundColor="#070a12"

        nodeLabel="name"

        nodeRelSize={6}

        linkColor={() =>
          "rgba(85,230,209,0.25)"
        }

        linkWidth={(link) =>
          Math.max(
            0.5,
            link.weight * 2
          )
        }

        nodeCanvasObject={(
          node,
          context,
          globalScale
        ) => {

          const label = node.name;

          const fontSize =
            12 / globalScale;

          context.font =
            `${fontSize}px DM Sans`;

          context.fillStyle =
            "#55e6d1";

          context.beginPath();

          context.arc(
            node.x,
            node.y,
            5,
            0,
            2 * Math.PI
          );

          context.fill();

          if (globalScale > 1.5) {

            context.fillStyle =
              "#f4f7ff";

            context.fillText(
              label,
              node.x + 7,
              node.y + 3
            );

          }

        }}
      />

    </div>
  );
}

export default IntelligenceGraph;