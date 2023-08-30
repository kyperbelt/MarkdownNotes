---
title: Monitoring and Alarms
---
# Monitoring and Alarms

### Things to learn on my own

- How to aggregate metrics?
- Alternatives to use for aggregating metrics, setting alarms?

## What is an Alarm
An alarm is a regional, top-level **aggregate** alarm that will, at a glance, confirm that a service is healthy and doing useful work. An "aggregate" or "composite" alarm is one that watches other alarms instead of watching a metric directly. 

## Why Do we Need?

A well-constructoed aggregate alarm teaches the monitoring system how to watch the service dashboard for a deviation from normal operation, and will notice problems faster and more consistently than a human ever could. It will save you watching dashboards for deployments, and provide instant confirmation of service health whenever you need it.

Ultimately, the alarm is an answer to the question **How do I know if my service is working properly?**

### An **Aggregate** alarm
Only needs to be as good as the dashboard check that a human would do to be used as a rollback monitor.

## How do I make one?
To make an alarm that lets you know if a service is workign at a glance you must create an alarm for a region by: 

1. Find what alarms you already have.
2. Aggregate all existing alarms with the current rollback monitor.
3. Check dashboard for information commonly looked at to determine useful working behavior.
4. Decide if all the monitors are configured well and the alarm is 'complete'. 

## What does a good alarm do?

It monitors: 

1. The Service
2. Resources
3. Other Monitors 

## Why Are region specific alarms important?

They are important because:

- Regions are isolated compute stacks that should fail and alarm separately.
- Different regions may have different thresholds based on traffic patterns, load, and latency.
- A regional alarm can be used for region-specific automated deployment rollbacks.
- Region alarms also help oncall to localize the problem and quickly confirm that other regions are still healthy.

## Metrics to Include

### Costumer Experience 

- Latency 
- Error Metrics

## Granularity & Datapoints

### Evaluiating monitor configuration

Configuring a monitor appropriately is as important as selecting the right metrics to alarm on. There are rules and rules-of-thumb, but, ultimiately, you need to use judgement and expertise to configure a monitor. You want the monitor to be sensitive engough to alarm quickly when there's customer impact, but not so sensitive that it causes intense pager pain for the supporting team. If the settings make sense but still cause pager pain, then it is a sign to fix the underlying problem.

**Evaluating metric configuration**

- Make sure that it is possible (numerically) to alarm.
- Is the threshold too high? 
- Will it take to long to alarm? rollback alarms should be more granular. 
- Threshold must be based on data.
- Should not be too sensitive.

### How quickly will that monitor alarm?

Response speed is important for customer impacting issues. Outage minutes are directly tied to lost revenue. Resolving issues quickly is important for the business and customer trust. We should configure monitors to alarm promptly. 

**variables that influence time to alarm:**

- **Metric Granularity** - Period or resolution. 
  <br/>How often a metric is aggregated to a single datapoint. Most services have many requests per minute.
- **Datapoint Count**

## Setting Thresholds for metric monitors

### How do you pick a threshold?

### Percentage Thresholds are useful
