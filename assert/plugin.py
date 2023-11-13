# -*- coding: utf-8 -*-
from typing import Optional, List

from pydantic import BaseModel, Field, model_validator


class PluginExport(BaseModel):
    class Install(BaseModel):
        shell: Optional[str] = Field(..., title="shell安装命令")
        pypi: Optional[str] = Field(..., title="pypi安装命令")
        github: Optional[str] = Field(None, title="github安装命令")

        @model_validator(mode="after")
        def available_check(self):
            if not any([self.shell, self.pypi, self.github]):
                raise ValueError("At least one of install must be available")
            return self

    plugin_name: str = Field(..., title="插件名称")
    plugin_link: str = Field(..., title="插件链接")
    plugin_desc: str = Field(..., title="插件描述")
    plugin_functions: List[str] = Field(..., title="插件功能")
    org_id: Optional[str] = Field(None, title="组织ID")
    author_id: str = Field(..., title="作者ID")
    plugin_install: Install = Field(..., title="插件安装方式")


EXPORT = [
    PluginExport(
        plugin_name="llmbot_plugin_bilisearch",
        plugin_link="https://github.com/LlmKira/llmbot_plugin_bilisearch",
        plugin_desc="通过自然语言调用哔哩哔哩搜索",
        plugin_functions=[
            "search_in_bilibili"
        ],
        org_id=None,
        author_id="sudoskys",
        plugin_install=PluginExport.Install(
            shell="pip3 install llmbot_plugin_bilisearch",
            pypi="llmbot_plugin_bilisearch",
            github=None,
        )
    )
]
