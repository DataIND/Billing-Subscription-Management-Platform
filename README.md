# 🧾 Billing & Subscription Management Platform

A **production-grade billing backend** inspired by Stripe, built with **Django**, **Django REST Framework**, **Celery**, **PostgreSQL**, **Redis**, and **Docker**.

This project demonstrates how to design a **financially correct**, **scalable**, and **resilient** billing system using patterns found in real-world SaaS platforms.

---

## 🚀 Motivation

Billing systems rarely fail due to missing features — they fail due to **incorrect financial behavior**.

Common failure modes in production systems include:
- Double charges caused by retries
- Race conditions during invoice generation
- Incorrect proration during plan changes
- Non-idempotent payment and webhook handling
- Mutable financial records that break auditability

This project is designed **correctness-first**, prioritizing safety, determinism, and auditability over convenience.

---

## 🎯 Goals & Non-Goals

### Goals
- Demonstrate safe billing architecture patterns
- Model subscriptions and billing as explicit domain logic
- Ensure financial correctness under retries and concurrency
- Mirror real SaaS billing workflows (subscriptions, invoices, payments)

### Non-Goals
- Processing real payments
- PCI-compliant card storage
- Production payment provider integrations

This is an **architectural and educational system**, not a payment processor.

---

## 🧠 Core Concepts & Invariants

### Key Concepts
- Subscription lifecycle modeled as a **finite state machine**
- **Append-only** financial records
- **Immutable** paid invoices
- **Idempotent** external-facing operations
- Async billing workflows with retries
- Explicit audit logging for financial events

### Financial Invariants
- Financial records are never deleted
- Paid invoices never change
- Adjustments are modeled as new invoices
- Balances are derived, not stored
- Retries must never create duplicate charges

These invariants are enforced at the domain and persistence layers.

---

## 🏗️ Architecture Overview

### Tech Stack

| Layer          | Technology                     |
|----------------|--------------------------------|
| API            | Django + Django REST Framework |
| Database       | PostgreSQL                     |
| Async Jobs     | Celery + RabbitMQ              |
| Cache          | Redis                          |
| Auth           | JWT                            |
| Infrastructure | Docker                         |
| Testing        | Pytest                         |

---

### High-Level Billing Flow

1. Subscriptions define billing behavior and pricing rules  
2. Billing cycles trigger invoice generation asynchronously  
3. Payments are processed via background workers  
4. Failures trigger retries and controlled state transitions  
5. Every financial mutation is audit-logged  

---

## 📦 Application Structure

```text
billing/
├── apps/
│   ├── accounts/        # Customers & billing profiles
│   ├── products/        # Products & plans
│   ├── pricing/         # Flat, tiered & usage pricing
│   ├── subscriptions/  # Subscription lifecycle
│   ├── invoices/       # Invoices & line items
│   ├── payments/       # Payment processing
│   ├── usage/           # Usage-based billing
│   ├── discounts/      # Coupons & promotions
│   ├── audit/           # Financial audit logs
│   └── webhooks/        # Payment provider events
│
├── core/
│   ├── services/        # Domain business logic
│   ├── workflows/       # Async billing workflows
│   ├── state_machines/  # Subscription FSM definitions
│   ├── idempotency.py   # Idempotent request handling
│   └── exceptions.py
│
├── config/
└── manage.py

