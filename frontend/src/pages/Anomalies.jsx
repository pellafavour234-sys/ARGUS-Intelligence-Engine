import { useEffect, useState } from "react";

import { getAnomalies } from "../services/api";


function Anomalies() {

  const [
    anomalies,
    setAnomalies,
  ] = useState([]);


  useEffect(() => {

    getAnomalies()
      .then((data) =>
        setAnomalies(
          data.items || []
        )
      )
      .catch(console.error);

  }, []);


  return (
    <div className="anomalies-page">

      <div className="page-heading">

        <span className="panel-kicker">
          DETECTION ENGINE
        </span>

        <h2>
          Anomalies
        </h2>

        <p>
          Behavioral deviations detected
          by ARGUS.
        </p>

      </div>


      <div className="anomaly-grid">

        {anomalies.length === 0 ? (

          <div className="empty-state">

            <div>
              ◇
            </div>

            <h3>
              No anomalies detected
            </h3>

            <p>
              Run a simulation to populate
              the detection engine.
            </p>

          </div>

        ) : (

          anomalies.map(
            (anomaly) => (

              <div
                className="anomaly-card"
                key={anomaly.id}
              >

                <span>
                  ANOMALY
                </span>

                <strong>
                  {anomaly.entity_id}
                </strong>

                <div>
                  Score:
                  {" "}
                  {anomaly.anomaly_score}
                </div>

                <p>
                  {anomaly.explanation}
                </p>

              </div>

            )
          )

        )}

      </div>

    </div>
  );
}

export default Anomalies;