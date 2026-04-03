# Reddit API Approval Kit

This folder contains a conservative, policy-aligned starter kit for requesting access to Reddit's traditional OAuth Data API for personal research and development.

## Purpose

This project is for **personal-use research** on public Reddit posts and comments via Reddit's OAuth-based Data API.

It is designed to present a narrow, low-risk use case:

- read public posts and comments
- summarize discussions for internal research
- identify recurring themes and sentiment
- avoid resale, redistribution, surveillance, and ML training

## Intended Use

- personal development and testing
- internal research only
- public content only
- low-volume API usage

## Not Intended For

- reselling Reddit data
- redistributing Reddit content in bulk
- creating shadow profiles on users
- training machine learning models on Reddit content
- masking identity, user agent, or OAuth credentials

## Suggested app form values

**Name**: Personal Reddit Research Tool

**Type**: script

**Description**: Personal-use script for reading public Reddit posts and comments through Reddit's API for research, summarization, and trend analysis. Not for resale, redistribution, or training machine learning models.

**About URL**: Link to this repository or your GitHub profile

**Redirect URI**: http://localhost:8080

## Repository contents

- `app-profile.md` - short product-style description suitable for a form or review
- `.env.example` - placeholder environment variables
- `example.py` - minimal OAuth-backed PRAW example
- `compliance-notes.md` - how the project stays conservative and low-risk

## Notes

This repo is meant to improve clarity and credibility, not to guarantee approval. Reddit retains discretion over API access and may change its requirements over time.
