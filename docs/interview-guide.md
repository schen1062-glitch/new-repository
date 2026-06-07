# Interview Guide - Portfolio Q&A

## 通用问题

### Q：为什么选择 n8n 而不是 Zapier / Make？

A：n8n 支持自托管，适合企业数据合规场景；Webhook + Error Trigger + 自定义代码节点组合灵活，成本可控，适合 $60k-$85k 远程自动化工程师岗位要求的生产级交付能力。

### Q：你如何保证工作流的生产可靠性？

A：每个作品均包含 Input Validation、Retry、Error Trigger 全局兜底、Audit Log 和标准化 Webhook 响应，符合可配置、可观测、可交付三原则。

### Q：ngrok 地址变了怎么办？

A：通过 `.env` 统一管理 `WEBHOOK_URL`，变更后 `docker compose restart n8n` 即可；长期交付推荐 n8n Cloud 或 Cloudflare Tunnel 固定域名。详见 [infrastructure.md](infrastructure.md)。

---

## AI Lead Qualification Agentic Orchestrator

### Q：这和普通线索评分自动化有什么区别？

A：引入了 Supervisor Agent 做规划与决策，不是简单 if/else 规则。n8n 负责 Orchestration 层（触发、路由、日志、错误恢复），体现 Agentic 思维而非线性脚本。

### Q：如何扩展到真实 LLM？

A：当前 Supervisor 节点可替换为 OpenAI / Claude Agent 节点，Audit Log 和 Error Trigger 架构无需改动，只需扩展 Tool Calling 和 Memory 模块。

### Q：企业微信通知失败怎么处理？

A：节点级 Retry + 全局 Error Trigger 双保险，失败记录到 Executions 面板，可扩展二次告警渠道。

---

## Intelligent Alert Escalation System

### Q：为什么使用 Respond to Webhook 节点？

A：飞书/外部系统需要快速返回 200 响应，否则会重试。我们确保在 1 秒内响应，符合最佳实践。

### Q：如何处理错误？

A：节点级 error 输出 + 全局 Error Trigger 双保险，失败时记录日志并可扩展告警。

### Q：如何扩展到多渠道？

A：当前用企业微信，可轻松并行添加 Telegram / Email / Slack（Switch 节点路由 severity 级别）。

### Q：告警升级逻辑如何设计？

A：Webhook 接收 → 数据标准化 + Validation → 按 severity 条件路由 → 企业微信通知 + Retry，全程可观测。

---

## Automated Compliance & Audit Trail Workflow

### Q：如何满足 GDPR / SOC2 / 中国网络安全法？

A：每次操作自动记录时间、用户、操作类型、实体，高危操作（如 delete）触发实时告警，形成完整审计闭环。

### Q：审计日志如何持久化？

A：Phase 2 已做持久化准备，可对接 PostgreSQL / Google Sheets / 企业 SIEM，工作流 Variables 统一管理配置。

### Q：合规规则引擎如何扩展？

A：Switch 节点 + Code 节点实现规则判断，新增合规规则只需加分支，无需重构主流程。

---

## 面试演示建议

1. **导入 workflow.json** → Publish → 展示 Executions 面板
2. **Console 发送测试请求** → 展示企业微信收到通知
3. **故意发送错误数据** → 展示 Validation 和 Error Trigger 兜底
4. **打开 docs/infrastructure.md** → 说明 ngrok 和生产部署方案
