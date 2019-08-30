# schema/init.py
# --------------
# Initializes the schema plugins. 

# Contents
# --------
# This plugin will define the following functions
# - ext.schema.showProcedures([schema], [session])

from ext.mysqlsh_plugins_common import register_plugin
from ext.schema import src as schema_src
from ext.schema import delproc as schema_delproc

register_plugin("showProcedures", schema_src.show_procedures, 
    { 
        "brief": "Lists all stored procedures.",
        "parameters": [
            {
                "name": "schema",
                "brief": "The schema which to list the stored procedures from.",
                "type": "string",
                "required": False
            },
            {
                "name": "session",
                "brief": "The session to be used on the operation.",
                "type": "object",
                "classes": ["Session", "ClassicSession"],
                "required": False
            }
        ]
    },
    "schema", 
    {
        "brief": "Schema management and utilities.",
        "details": [
            "A collection of schema management tools and related "
            "utilities that work on schemas" 
        ]
    })
    
register_plugin("deleteProcedures", schema_delproc.delete_procedures, 
    { 
        "brief": "Delete stored procedures.",
        "parameters": [
            {
                "name": "schema",
                "brief": "The schema which to delete the stored procedures from.",
                "type": "string",
                "required": False
            },
            {
                "name": "routine",
                "brief": "The routine/procedure to be deleted..",
                "type": "string",
                "required": False
            },
            {
                "name": "session",
                "brief": "The session to be used on the operation.",
                "type": "object",
                "classes": ["Session", "ClassicSession"],
                "required": False
            }
        ]
    },
    "schema")
