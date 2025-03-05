import re
import yaml
import json
from typing import Literal, List, Dict, Any, Union, Optional
import logging

class MarkdownParser:
    """A parser class for extracting blocks from markdown content."""

    @staticmethod
    def extract_blocks(content: str, block_type: Literal["yaml", "json", "code"] = "code", loose: bool = False) -> List[str]:
        """
        Extract blocks from markdown content.
        
        Args:
            content: The markdown content
            block_type: Type of block to extract
            loose: If True and specific block not found, fallback to generic code block
            
        Returns:
            List of extracted block contents
        """
        if not content:
            return []
        
        match block_type:
            case "yaml":
                pattern = r'```\s*yaml\s*\n(.*?)\n```'
            case "json":
                pattern = r'```\s*json\s*\n(.*?)\n```'
            case "code":
                pattern = r'```(?:\w*)\s*\n(.*?)\n```'
            case _:
                raise ValueError(f"Unsupported block type: {block_type}")
        
        blocks = re.findall(pattern, content, re.DOTALL)
            
        # If no target blocks found and loose mode is enabled, try generic code blocks
        if not blocks and loose and block_type == "yaml":
            pattern = r'```\s*\n(.*?)\n```'
            blocks = re.findall(pattern, content, re.DOTALL)
            
            # Try to validate each block as YAML
            validated_blocks = []
            for block in blocks:
                try:
                    yaml.safe_load(block)
                    validated_blocks.append(block)
                except yaml.YAMLError:
                    pass
            
            blocks = validated_blocks
        
        return blocks
    
    @staticmethod
    def parse(
        content: str, 
        block_type: Literal["yaml", "json"] = "yaml", 
        mode: Literal["exact_one", "first_one"] = "exact_one", 
        loose: bool = True
    ) -> Union[Dict[str, Any], List[Any]]:
        """
        Parse markdown blocks into Python objects.
        
        Args:
            content: The markdown content
            block_type: Type of block to extract and parse
            mode: Validation mode for number of blocks found
            loose: If True, try generic code blocks if specific ones not found
            
        Returns:
            Parsed Python object (dict or list)
        """        
        blocks = MarkdownParser.extract_blocks(content, block_type, loose)
                
        if mode == "exact_one" and len(blocks) != 1:
            raise ValueError(f"Expected exactly one {block_type} block, found {len(blocks)}")
        if mode == "first_one" and len(blocks) == 0:
            raise ValueError(f"Expected at least one {block_type} block, found none")
            
        target_block = blocks[0]
        
        logging.info(target_block)
        
        match block_type:
            case "yaml":
                return yaml.safe_load(target_block)
            case "json":
                return json.loads(target_block)
            case _:
                raise ValueError(f"Unsupported block type: {block_type}")
