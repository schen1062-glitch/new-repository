# Intelligent Alert Escalation System - Mid Commercial v6 (Phase 1-3 Optimized)

## 业务痛点

重要告警需要按严重程度推送，避免遗漏。

## 核心功能

- Webhook 接收告警
- 数据标准化 + Validation
- 企业微信通知 + Retry
- 完整 Error Trigger + 日志
- Phase 1-3 优化：企业微信切换、Retry、Validation、日志加强

## 配置步骤

1. 企业微信 Key 已内置（推荐 Credential）
2. Production URL: `/webhook/alert-escalation`
3. Publish 工作流

## 测试方法

```javascript
fetch("https://您的ngrok地址/webhook/alert-escalation", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    severity: "high",
    message: "测试告警",
    alertId: "TEST-001"
  })
}).then(r => r.text()).then(console.log);
```

## 技术亮点（面试卖点）

- Webhook + Respond 最佳实践（1 秒内响应，避免外部系统重试）
- 条件化通知 + 错误恢复机制（节点级 error 输出 + 全局 Error Trigger）
- 配置化设计，便于客户二次开发
- 生产级可观测性（Error Trigger + Log）

## ngrok 地址变更处理

见 [docs/infrastructure.md](../docs/infrastructure.md)
