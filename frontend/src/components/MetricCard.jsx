function MetricCard({
  label,
  value,
  change,
  icon,
  status = "neutral",
}) {
  return (
    <div className={`metric-card ${status}`}>
      <div className="metric-card__top">
        <span className="metric-card__label">
          {label}
        </span>

        <span className="metric-card__icon">
          {icon}
        </span>
      </div>

      <div className="metric-card__value">
        {value}
      </div>

      {change && (
        <div className="metric-card__change">
          {change}
        </div>
      )}
    </div>
  );
}

export default MetricCard;