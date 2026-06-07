# AI Lead Qualification Agentic Orchestrator - Mid Commercial v2

**业务场景**：销售团队每天接收大量线索，需要 AI 自动评分、规划处理步骤，并实时通知销售跟进，提高转化率。

## 核心功能

- Webhook 接收新线索（支持飞书表单等）
- Supervisor Agent（Planning & Decision）进行自主评分 + 质量判断 + 处理计划
- 企业微信实时通知
- Audit Log 审计记录
- 完整错误处理（Error Trigger + Retry）

## 技术亮点（面试卖点）

- 真正的 **Agentic Orchestration**：Supervisor Agent 模拟规划决策，而非简单规则判断
- n8n 作为可靠 Orchestration 层（Webhook Trigger + Routing + Logging + Error Recovery）
- 生产级设计：Retry 机制、标准化输出、易扩展（后续可加 Memory / Tool Calling / 真实 LLM Agent）
- 从线性流程升级到 Agentic 思维，体现 AI + 业务流程结合能力

## 配置说明

1. 替换企业微信 Webhook Key（推荐创建 Credential）
2. Production Webhook Path：`/webhook/lead-agentic`
3. 推荐长期使用固定域名（n8n Cloud 或 Cloudflare Tunnel）

## 测试方法

浏览器 Console 执行：

```javascript
fetch("https://您的ngrok地址/webhook/lead-agentic", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    name: "李总监",
    company: "字节跳动",
    source: "飞书表单"
  })
}).then(r => r.text()).then(console.log).catch(console.error);
```

## ngrok / 重启处理

1. 启动 ngrok：`ngrok http --host-header=rewrite http://localhost:5678`
2. 更新 `.env` 中的 `WEBHOOK_URL` 和 `N8N_HOST`
3. `docker compose restart n8n`

## Phase 优化历程

- **Phase 1**：企业微信集成 + Input Validation + Retry
- **Phase 2**：日志加强 + 可观测性
- **Phase 3**：Agentic Supervisor + Error Trigger
