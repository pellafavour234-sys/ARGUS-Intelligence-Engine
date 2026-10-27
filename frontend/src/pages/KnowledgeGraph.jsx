import IntelligenceGraph
  from "../graph/IntelligenceGraph";


function KnowledgeGraph() {

  return (
    <div className="graph-page">

      <div className="page-heading">

        <span className="panel-kicker">
          GRAPH INTELLIGENCE
        </span>

        <h2>
          Knowledge Graph
        </h2>

        <p>
          Explore relationships discovered
          inside the ARGUS environment.
        </p>

      </div>

      <div className="graph-container">

        <IntelligenceGraph />

      </div>

    </div>
  );
}

export default KnowledgeGraph;