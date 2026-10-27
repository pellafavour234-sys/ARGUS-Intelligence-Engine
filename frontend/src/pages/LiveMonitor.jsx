import { useEffect, useState } from "react";


function LiveMonitor() {

  const [events, setEvents] = useState([]);

  useEffect(() => {

    const socket = new WebSocket(
      "ws://127.0.0.1:8000/api/live"
    );

    socket.onmessage = (message) => {

      const event =
        JSON.parse(message.data);

      setEvents((previous) => [
        event,
        ...previous,
      ].slice(0, 30));

    };

    return () => socket.close();

  }, []);


  return (
    <div className="monitor-page">

      <div className="page-heading">

        <span className="panel-kicker">
          REAL-TIME INTELLIGENCE
        </span>

        <h2>Live Monitor</h2>

        <p>
          Continuous event intelligence stream.
        </p>

      </div>


      <div className="live-stream">

        {events.map((event, index) => (

          <div
            className={
              event.anomaly
                ? "stream-event anomaly"
                : "stream-event"
            }
            key={index}
          >

            <span className="stream-time">
              LIVE
            </span>

            <strong>
              {event.entity}
            </strong>

            <span>
              {event.event}
            </span>

            <span>
              {event.value}
            </span>

            {event.anomaly && (
              <span className="alert">
                ANOMALY
              </span>
            )}

          </div>

        ))}

      </div>

    </div>
  );
}

export default LiveMonitor;