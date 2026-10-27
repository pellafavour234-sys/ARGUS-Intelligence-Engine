import { useState } from "react";

import Sidebar from "./components/Sidebar";
import TopBar from "./components/TopBar";

import Dashboard from "./pages/Dashboard";
import LiveMonitor from "./pages/LiveMonitor";
import KnowledgeGraph from "./pages/KnowledgeGraph";
import Anomalies from "./pages/Anomalies";
import SimulationLab from "./pages/SimulationLab";

import "./styles/global.css";


function App() {

  const [
    activePage,
    setActivePage,
  ] = useState("dashboard");


  function renderPage() {

    switch (activePage) {

      case "monitor":
        return <LiveMonitor />;

      case "graph":
        return <KnowledgeGraph />;

      case "anomalies":
        return <Anomalies />;

      case "simulation":
        return <SimulationLab />;

      case "dashboard":
      default:
        return <Dashboard />;
    }
  }


  return (
    <div className="app">

      <Sidebar
        activePage={activePage}
        onNavigate={setActivePage}
      />

      <div className="main">

        <TopBar />

        {renderPage()}

      </div>

    </div>
  );
}


export default App;