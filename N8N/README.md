# n8n 中级商业可交付案例

本目录包含三个基于 n8n 自托管的工作流案例，面向国际客户集成场景，均达到中级商业可交付水平。

## 案例清单

| 序号 | 案例 | 核心能力 |
|------|------|----------|
| 1 | [AI Lead Qualification Agentic Orchestrator](n8n-ai-lead-qualification/) | Agentic Orchestration + 企业微信通知 |
| 2 | [Intelligent Alert Escalation System](n8n-intelligent-alert-escalation/) | 多渠道智能告警升级 |
| 3 | [Automated Compliance & Audit Trail Workflow](n8n-automated-compliance-audit/) | 合规审计与日志追踪 |

## 技术栈

- n8n（Docker 自托管）+ Agentic Workflow
- 企业微信、飞书 Webhook 集成
- Error Trigger、Audit Log、Retry 机制
- ngrok + Docker Compose（见 [docs/infrastructure.md](docs/infrastructure.md)）

## 快速开始

- 所有工作流均为 `workflow.json`，可直接导入 n8n
- 测试方法见各案例文件夹 `README.md`
- 面试 Q&A 见 [docs/interview-guide.md](docs/interview-guide.md)

## 相关作品

- Coze 国内智能体案例见同级目录：[../coze/](../coze/)
