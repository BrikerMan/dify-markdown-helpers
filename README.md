# Markdown Helpers

**Author:** eliyar-eziz  
**Version:** 0.0.1  
**Type:** Dify Plugin Tool

## Overview

Markdown Helpers is a Dify plugin designed to simplify the extraction of structured data (JSON/YAML) from markdown text, particularly useful when working with LLM responses. This plugin provides two main functions that help parse and extract structured data from code blocks within markdown content.

## Features

### 1. Extract JSON/YAML

Extracts and parses JSON or YAML code blocks from Markdown text, returning the structured data as a response.

**Parameters:**

- `markdown_text` (string, required): The Markdown text containing JSON or YAML code blocks to extract.
- `format_type` (select, optional): The format type to extract - either "json" or "yaml". Default: "json".
- `mode` (select, optional): The extraction mode:
  - `first_one`: Extract the first matching code block found (default)
  - `exact_one`: Require exactly one matching code block
- `loose` (boolean, optional): If true, will try to extract from generic code blocks if specific format blocks are not found. Default: true.

**Output:**

- Returns a JSON object with the parsed data and success status.
- Sets two variables:
  - `success`: Boolean indicating whether the extraction was successful

### 2. Extract JSON/YAML & Next Step

Similar to the first function but additionally extracts a "next_step" field from the structured data, useful for workflow automation.

**Parameters:**

- `markdown_text` (string, required): The Markdown text containing JSON or YAML code blocks to extract.
- `format_type` (select, optional): The format type to extract - either "json" or "yaml". Default: "json".
- `mode` (select, optional): The extraction mode:
  - `first_one`: Extract the first matching code block found (default)
  - `exact_one`: Require exactly one matching code block
- `loose` (boolean, optional): If true, will try to extract from generic code blocks if specific format blocks are not found. Default: true.

**Output:**

- Returns the parsed data as a JSON object
- Sets two variables:
  - `next_step`: The value of the "next_step" field from the parsed data
  - `success`: Boolean indicating whether the extraction was successful
