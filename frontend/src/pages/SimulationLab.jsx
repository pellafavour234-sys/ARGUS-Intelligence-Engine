import { useState } from "react";

import { generateEvents } from "../services/api";


const scenarios = [
  "normal",
  "activity_spike",
  "behavior_shift",
  "network_formation",
  "coordinated_activity",
];


function SimulationLab() {

  const [
    scenario,
    setScenario,
  ] = useState("normal");

  const [
    eventCount,
    setEventCount,
  ] = useState(100);

  const [
    result,
    setResult,
  ] = useState(null);


  async function runSimulation() {

    try {

      const data =
        await generateEvents(
          Number(eventCount)
        );

      setResult(data);

    } catch (error) {

      console.error(error);

    }

  }


  return (
    <div className="simulation-page">

      <div className="page-heading">

        <span className="panel-kicker">
          CONTROL CENTER
        </span>

        <h2>
          Simulation Lab
        </h2>

        <p>
          Inject controlled behavioral
          scenarios into the intelligence world.
        </p>

      </div>


      <div className="simulation-card">

        <label>
          SCENARIO
        </label>

        <select
          value={scenario}
          onChange={(event) =>
            setScenario(
              event.target.value
            )
          }
        >

          {scenarios.map(
            (item) => (
              <option
                value={item}
                key={item}
              >
                {item}
              </option>
            )
          )}

        </select>


        <label>
          EVENT COUNT
        </label>

        <input
          type="number"
          min="10"
          max="10000"
          value={eventCount}
          onChange={(event) =>
            setEventCount(
              event.target.value
            )
          }
        />


        <button
          className="simulation-button"
          onClick={runSimulation}
        >
          RUN INTELLIGENCE SIMULATION
        </button>


        {result && (

          <div className="simulation-result">

            <strong>
              Simulation completed
            </strong>

            <span>
              Events:
              {" "}
              {result.generated}
            </span>

            <span>
              Entities:
              {" "}
              {result.world.entities}
            </span>

            <span>
              Relationships:
              {" "}
              {result.world.relationships}
            </span>

          </div>

        )}

      </div>

    </div>
  );
}

export default SimulationLab;