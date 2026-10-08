# Procurement agent design

Evaluate the procurement case in `case/` and prepare an evidence-based recommendation and a leadership slide.

## Instructions for the running agent

For teaching purposes, run only **Verify → Draft → Review**. Ingest is the earlier brief-writing activity and is outside this run.

Before starting, check for `BRIEF.md` in the student workspace. If it is available, use it as the procurement requirements and evaluation criteria, preserving its source references and unresolved questions. Do not regenerate it or change its criteria based on the bids. If it is missing, pause and ask the user to generate `BRIEF.md` using the earlier brief-writing exercise, without access to submitted bids or earlier evaluation results. Resume only once the brief is available; do not run Ingest automatically.

Act as the orchestrator and use your built-in subagent tools to run the tasks below. Do not write orchestration code or make direct API calls. Pass each subagent only the inputs it needs, collect its results, and pass those results to the next stage.

## Workflow

1. **Verify:** one subagent per bidder (Aperture, Helix, Meridian, Northstar, Peregrine) receives `BRIEF.md` and only that bidder's submission. It evaluates each criterion and recommends pass or fail for each mandatory gate, with supporting evidence. Separate bidder contexts help avoid mixing details between bids.
2. **Draft:** one subagent synthesises the verification results and scores only eligible bids. Check mandatory gates before weighted scoring.
3. **Review:** one subagent writes the result out to a leadership slide, including the recommendation, supporting evidence, and unresolved issues.

## Basic boundaries

- Use the supplied case evidence and preserve references to the documents and their locations. Flag missing or conflicting evidence; do not invent facts or amendments.
- Keep award decisions with the committee and bidder contact with Procurement approval.
- Record the student's agreed access limits, permitted tools, human approvals, stop conditions, and evidence logs in this file as the design develops. Record execution and review findings here after running the workflow.
