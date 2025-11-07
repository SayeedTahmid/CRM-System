import React from "react";

type ReportCardsProps = {
  metrics: {
    totalDeals: number;
    wonDeals: number;
    activitiesThisWeek: number;
    revenueForecast: number;
  };
};

const formatter = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 });

export function ReportCards({ metrics }: ReportCardsProps) {
  return (
    <div className="grid dashboard">
      <div className="card">
        <h3>Total Deals</h3>
        <p style={{ fontSize: "2rem", margin: 0 }}>{metrics.totalDeals}</p>
        <p style={{ margin: 0, color: "rgba(226,232,240,0.65)" }}>Deals across all pipelines</p>
      </div>
      <div className="card">
        <h3>Won Deals</h3>
        <p style={{ fontSize: "2rem", margin: 0 }}>{metrics.wonDeals}</p>
        <p style={{ margin: 0, color: "rgba(226,232,240,0.65)" }}>Closed deals this month</p>
      </div>
      <div className="card">
        <h3>Activities</h3>
        <p style={{ fontSize: "2rem", margin: 0 }}>{metrics.activitiesThisWeek}</p>
        <p style={{ margin: 0, color: "rgba(226,232,240,0.65)" }}>Completed this week</p>
      </div>
      <div className="card">
        <h3>Forecast</h3>
        <p style={{ fontSize: "2rem", margin: 0 }}>{formatter.format(metrics.revenueForecast)}</p>
        <p style={{ margin: 0, color: "rgba(226,232,240,0.65)" }}>Expected closing value</p>
      </div>
    </div>
  );
}
