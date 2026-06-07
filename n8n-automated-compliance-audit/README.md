# Automated Compliance & Audit Trail Workflow - Mid Commercial v3 (Phase 1-3 Optimized)

## 业务场景

企业数据操作需满足合规要求（GDPR/SOC2/中国网络安全法），自动记录审计轨迹、检测高危操作并告警。

## 核心功能

- 操作审计记录（时间、用户、操作类型、合规判断）
- 高危操作实时企业微信告警
- 审计日志写入 + 持久化准备
- Input Validation + Retry + Error Trigger
- Phase 1-3 优化：Credential 风格、企业微信切换、Retry、Validation、日志加强

## 配置说明

1. 企业微信 Key 已内置（推荐改为 Credential）
2. Production Webhook URL：`/webhook/compliance-audit`
3. 测试数据示例：

```json
{
  "operation": "delete",
  "user": "admin",
  "entity": "客户记录"
}
```

## 测试方法

```javascript
fetch("https://您的ngrok地址/webhook/compliance-audit", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    operation: "delete",
    user: "admin",
    entity: "客户记录"
  })
}).then(r => r.text()).then(console.log);
```

## 技术亮点（面试卖点）

- 完整审计日志闭环 + 合规规则引擎
- 错误处理与可观测性（Retry + Error Trigger）
- Phase 1-3 优化后达到中级商用标准
- 符合国内外合规需求，可直接交付

## ngrok 地址变更处理

见 [docs/infrastructure.md](../docs/infrastructure.md)
