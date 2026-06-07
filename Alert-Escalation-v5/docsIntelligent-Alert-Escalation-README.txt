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
2. Production URL: /webhook/alert-escalation
3. Publish 工作流

## ngrok 地址变更处理
（同下方专项标注）

## 测试方法
fetch("https://nonparentally-unfagged-huong.ngrok-free.dev/webhook/alert-escalation", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ severity: "high", message: "测试告警", alertId: "TEST-001" })
}).then(r => r.text()).then(console.log);