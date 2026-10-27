function TopBar() {
  return (
    <header className="topbar">

      <div>
        <div className="topbar__eyebrow">
          ADAPTIVE INTELLIGENCE
        </div>

        <h1>
          System Overview
        </h1>
      </div>

      <div className="topbar__right">

        <div className="live-indicator">
          <span className="pulse" />
          LIVE
        </div>

        <div className="avatar">
          A
        </div>

      </div>

    </header>
  );
}

export default TopBar;