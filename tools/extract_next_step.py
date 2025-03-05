from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.markdown_base_parser import MarkdownParser
from tools.utils import logger


class ExtractJsonYamlNEextStepTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        markdown_text = tool_parameters.get("markdown_text", "")
        format_type = tool_parameters.get("format_type", "json")
        loose = tool_parameters.get("loose", True)
        mode = tool_parameters.get("mode", "first_one")

        logger.debug(f"Received params {tool_parameters}")
        logger.debug(f"Received markdown text: {markdown_text}")

        if not markdown_text:
            yield self.create_variable_message("next_step", None)
            yield self.create_variable_message("success", False)
            yield self.create_json_message({"error": "No markdown text provided"})
            return

        try:
            # Use the MarkdownParser to extract and parse the content
            parsed_data = MarkdownParser.parse(
                content=markdown_text,
                block_type=format_type,
                mode=mode,
                loose=loose,
            )

            yield self.create_variable_message("next_step", parsed_data.get("next_step"))
            yield self.create_variable_message("success", True)
            yield self.create_json_message(parsed_data)
        except Exception as e:
            yield self.create_variable_message("next_step", None)
            yield self.create_variable_message("success", False)
            yield self.create_json_message({"error": str(e)})
