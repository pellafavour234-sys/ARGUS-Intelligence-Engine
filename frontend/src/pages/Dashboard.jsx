import { useEffect, useState } from "react";

import MetricCard from "../components/MetricCard";
import { getDashboard } from "../services/api";


function Dashboard() {

  const [data, setData] = useState(null);

  useEffect(() => {

    getDashboard()
      .then(setData)
      .catch((error) => {
        console.error(
          "Failed to load dashboard:",
          error
        );
      });

  }, []);


  if (!data) {
    return (
      <div className="loading-screen">
        <div className="loader" />
        <span>
          INITIALIZING INTELLIGENCE ENGINE...
        </span>
      </div>
    );
  }


  return (
    <main className="dashboard">

      <section className="metrics-grid">

        <MetricCard
          label="ENTITIES"
          value={data.entities.toLocaleString()}
          icon="◎"
        />

        <MetricCard
          label="RELATIONSHIPS"
          value={data.relationships.toLocaleString()}
          icon="⌁"
        />

        <MetricCard
          label="EVENTS PROCESSED"
          value={data.events.toLocaleString()}
          icon="◈"
          status="positive"
        />

        <MetricCard
          label="ANOMALIES"
          value={data.anomalies}
          icon="△"
          status="warning"
        />

      </section>


      <section className="dashboard-grid">

        <div className="panel graph-panel">

          <div className="panel-header">

            <div>
              <span className="panel-kicker">
                NETWORK INTELLIGENCE
              </span>

              <h2>
                Relationship Graph
              </h2>
            </div>

            <span className="panel-live">
              LIVE
            </span>

          </div>

          <div className="graph-placeholder">

            <div className="graph-orb orb-one" />
            <div className="graph-orb orb-two" />
            <div className="graph-orb orb-three" />

            <div className="graph-center">
              GRAPH ENGINE
            </div>

          </div>

        </div>


        <div className="panel activity-panel">

          <div className="panel-header">

            <div>
              <span className="panel-kicker">
                SYSTEM STREAM
              </span>

              <h2>
                Live Activity
              </h2>
            </div>

          </div>

          <div className="activity-list">

            <div className="activity-item">
              <span className="activity-dot" />
              <div>
                <strong>
                  Intelligence engine online
                </strong>

                <small>
                  System initialized successfully
                </small>
              </div>
            </div>

            <div className="activity-item">
              <span className="activity-dot" />
              <div>
                <strong>
                  Anomaly detector ready
                </strong>

                <small>
                  Isolation Forest loaded
                </small>
              </div>
            </div>

            <div className="activity-item">
              <span className="activity-dot warning" />
              <div>
                <strong>
                  Simulation awaiting input
                </strong>

                <small>
                  No active scenario
                </small>
              </div>
            </div>

          </div>

        </div>

      </section>

    </main>
  );
}

export default Dashboard;