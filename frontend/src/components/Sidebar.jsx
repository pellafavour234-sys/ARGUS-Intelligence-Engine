function Sidebar({ activePage, onNavigate }) {
  const items = [
    ["dashboard", "Dashboard", "⌂"],
    ["monitor", "Live Monitor", "◉"],
    ["graph", "Knowledge Graph", "⌁"],
    ["anomalies", "Anomalies", "△"],
    ["analytics", "Analytics", "◫"],
    ["simulation", "Simulation Lab", "◈"],
  ];

  return (
    <aside className="sidebar">

      <div className="brand">
        <div className="brand__mark">
          A
        </div>

        <div>
          <div className="brand__name">
            ARGUS
          </div>

          <div className="brand__subtitle">
            INTELLIGENCE ENGINE
          </div>
        </div>
      </div>

      <nav className="navigation">

        <div className="navigation__label">
          CORE SYSTEM
        </div>

        {items.map(([id, label, icon]) => (
          <button
            key={id}
            className={
              activePage === id
                ? "nav-item active"
                : "nav-item"
            }
            onClick={() => onNavigate(id)}
          >
            <span className="nav-item__icon">
              {icon}
            </span>

            <span>{label}</span>
          </button>
        ))}

      </nav>

      <div className="sidebar__footer">

        <div className="system-status">
          <span className="status-dot" />
          <span>ENGINE ONLINE</span>
        </div>

        <span className="version">
          v1.0.0
        </span>

      </div>

    </aside>
  );
}

export default Sidebar;