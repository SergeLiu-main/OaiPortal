# Here is a instruction of `OaiPortal`

## What is it?

this is a project which is building, we designed it aims to provide a better utils or dev-tools for developers who are develop the app which is using openai_completions or openai_response like api.

---

# 这是 `OaiPortal` 的实用指南

## 它是什么

这是一个仍在构建中的项目, 它被设计来辅助开发者进行接入openai-response或completions格式的api的app的开发。

## 指南.

### 模块:

| Package Name | (simple) Instruction | Child Members |
| :-: | :- | :-: |
| network | 用于通用的网络操作，封装不同网络内核的行为，并保证最大兼容性 | cores/ |
| openai_utils | 主工具，用于openai-like的api服务，以openai库实现，后续可能支持以network模块实现 | null(planning) |
| types | **应由本包开发者使用**的类型模块，用户/一般开发者请使用暴露出的类型，我们确保它们足够 | network/ (expanding) |
| utils | 通用工具服务 | null(planning) |

