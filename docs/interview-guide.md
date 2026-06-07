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

## Coze Case 1 - 情感分析

### Q：为什么用 Code 节点而不是纯 Prompt 输出？

A：LLM 输出格式不稳定，Code 节点做 JSON 解析、字段校验和置信度归一化，保证下游 n8n/飞书对接可靠。

### Q：知识库放什么内容？

A：情感标签定义、边界案例、行业词典，减少模型自由发挥，提高一致性和可解释性。

---

## Coze Case 2 - 合同审查

### Q：为什么拆成两个知识库？

A：标准条款（完整性检查）与风险规则（等级判定）职责不同，分开维护便于法务独立更新，RAG 检索更精准。

### Q：如何避免 AI 给出错误法律建议？

A：Prompt 明确「辅助审查、不构成法律意见」，输出含 disclaimer；high 风险项建议人工复核。

---

## 面试演示建议

1. **n8n**：导入 workflow.json → Publish → Console 测试 → 企业微信通知
2. **Coze**：打开 Bot 链接 → 跑 2-3 条测试 → 展示结构化 JSON 输出
3. **对比讲述**：n8n 擅长集成与生产运维，Coze 擅长国内 Agent 快速交付
4. **打开 docs/infrastructure.md** → 说明 ngrok 和生产部署方案
