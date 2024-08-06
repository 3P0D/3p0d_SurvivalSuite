bl_info = {
    "name": "3P0D's Survival Suite",
    "author": "3P0D ON/OFF",
    "version": (0, 0, 1),
    "blender": (3, 6, 0),
    "location": "View3D > Tool",
    "description": "Lots of repetitive commands because I'm lazy.",
    "warning": "",
    "doc_url": "",
    "category": "View 3D",
}


import bpy

# ----------------------------------------------------------------



# ----------------------------------------------------------------

class LAZYSUITE_PT_main_panel(bpy.types.Panel):

    bl_label = "3P0D's Survival Suite 0.0.1"
    bl_idname = "LAZYSUITE_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3P0D's Survival Suite"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Because I'm lazy.")
        
        
class LAZYSUITE_PT_panelA(bpy.types.Panel):
    
    bl_label = "Apply changes on objects"
    bl_idname = "LAZYSUITE_PT_panelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3P0D's Survival Suite"
    bl_parent_id = "LAZYSUITE_PT_main_panel"
#    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Transforms:")
        row = layout.row()
        row.operator("lazysuite.applytransform", icon = 'CURVE_NCIRCLE')
        row.operator("lazysuite.cleartransform", icon='TRASH')
        row = layout.row()
        row.operator("lazysuite.applyrotation_rig", icon = 'TRACKING_REFINE_FORWARDS')
        row = layout.row()
        row.label(text="Geometry:")
        row = layout.row()
        row.operator("lazysuite.fixnormals", icon='ORIENTATION_NORMAL')
        row.operator("lazysuite.origintoselect", icon='PIVOT_CURSOR')
        row = layout.row()
        row.label(text="Parents:")
        row = layout.row()
        row.operator("lazysuite.makesingle", icon='ORPHAN_DATA')
        row.operator("lazysuite.clearparents", icon='GHOST_DISABLED')
        
class LAZYSUITE_PT_panelB(bpy.types.Panel):
    
    bl_label = "Add modifiers and objects"
    bl_idname = "LAZYSUITE_PT_panelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3P0D's Survival Suite"
    bl_parent_id = "LAZYSUITE_PT_main_panel"
#    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Add objects:")
        row = layout.row()
        row.operator("lazysuite.createempty", icon='EMPTY_AXIS')
        row.operator("lazysuite.createsuzanne", icon='MONKEY')
        row = layout.row()
        row.separator()
        row = layout.row()
        row.label(text="Add modifiers:")
        row = layout.row()
        row.operator("lazysuite.addmodifier_mirror", icon='MOD_MIRROR')
        row.operator("lazysuite.addmodifier_bevel", icon='MOD_BEVEL')
        row = layout.row()
        row.operator("lazysuite.addmodifier_shrinkwrap", icon='MOD_SHRINKWRAP')
        row = layout.row()
        sub = row.row()
        sub.scale_x = 0.75
        sub.prop(context.scene, 'prepsculpt_remesh')
        row.operator("lazysuite.prepsculpt", icon='SCULPTMODE_HLT')
        
class LAZYSUITE_PT_panelC(bpy.types.Panel):
    
    bl_label = "Add textures and materials"
    bl_idname = "LAZYSUITE_PT_panelC"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3P0D's Survival Suite"
    bl_parent_id = "LAZYSUITE_PT_main_panel"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Add checker texture:")
        row = layout.row()
        row.operator("lazysuite.addchecker_512")
        row.operator("lazysuite.addchecker_1024")
        row.operator("lazysuite.addchecker_2048")
        row.operator("lazysuite.addchecker_4096")
        row = layout.row()
        
class LAZYSUITE_PT_panelD(bpy.types.Panel):
    
    bl_label = "Set objects names"
    bl_idname = "LAZYSUITE_PT_panelD"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3P0D's Survival Suite"
    bl_parent_id = "LAZYSUITE_PT_main_panel"
#    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Set prefix:")
       
        row = layout.row()
        sub = row.row()
        sub.scale_x = 1.5
        sub.prop(context.scene, 'newName_geo')
        row.operator("lazysuite.applyname_geo")
       
        row = layout.row()
        sub = row.row()
        sub.scale_x = 1.5
        sub.prop(context.scene, 'newName_rig')
        row.operator("lazysuite.applyname_rig")
        
        row = layout.row()
        sub = row.row()
        sub.scale_x = 1.5
        sub.prop(context.scene, 'newName_empty')
        row.operator("lazysuite.applyname_empty")
        
        row = layout.row()
        sub = row.row()
        sub.scale_x = 1.5
        sub.prop(context.scene, 'newName_curve')
        row.operator("lazysuite.applyname_curve")
    
        row = layout.row()
        sub = row.row()
        sub.scale_x = 1.5
        sub.prop(context.scene, 'newName_bool')
        row.operator("lazysuite.applyname_bool")
    
        
# --------------------------------------------------------------------------------

class LAZYSUITE_OT_applyrotation_rig(bpy.types.Operator):
    
    bl_label = "Apply -90° (Rig)"
    bl_idname = "lazysuite.applyrotation_rig"
    bl_description = "Apply a -90° rotation on a rig to prepare it for export in Unity"
    def execute(self, context):
        if bpy.context.object.rotation_euler[0] != -1.570796:
            bpy.context.object.rotation_euler[0] = 0
            bpy.context.object.rotation_euler[1] = 0
            bpy.context.object.rotation_euler[2] = 0
            bpy.context.object.rotation_euler[0] = 1.5708
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.context.object.rotation_euler[0] = -1.5708
        elif bpy.context.object.rotation_euler[0] == -1.5708:
            pass
        return {'FINISHED'}
    
class LAZYSUITE_OT_applytransform(bpy.types.Operator):
    
    bl_label = "Apply all"
    bl_idname = "lazysuite.applytransform"
    bl_description = "Apply all the transform of an object: location, rotation, scale"
    def execute(self, context):
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        return {'FINISHED'}

    
class LAZYSUITE_OT_cleartransform(bpy.types.Operator):
    
    bl_label = "Clear all"
    bl_idname = "lazysuite.cleartransform"
    bl_description = "Clear all the transform of an object: location, rotation, scale"
    def execute(self, context):
        bpy.ops.object.location_clear(clear_delta=False)
        bpy.ops.object.rotation_clear(clear_delta=False)
        bpy.ops.object.scale_clear(clear_delta=False)
        return {'FINISHED'}
    
class LAZYSUITE_OT_fixnormals(bpy.types.Operator):
    
    bl_label = "Fix normals (Obj.Mode)"
    bl_idname = "lazysuite.fixnormals"
    bl_description = "Fix the inverted normals of an object instantly, in Object Mode"
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent(inside=False)
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

class LAZYSUITE_OT_origintoselect(bpy.types.Operator):
    
    bl_label = "Origin to selected"
    bl_idname = "lazysuite.origintoselect"
    bl_description = "Move the origin of the object to the selected vertex, edge, or face, in Edit Mode"
    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        return {'FINISHED'}
    
    
class LAZYSUITE_OT_makesingle(bpy.types.Operator):
    
    bl_label = "Make single (Userdata)"
    bl_idname = "lazysuite.makesingle"
    bl_description = "Break the bonds between the selected objects and their datas, making them all unique users"
    def execute(self, context):
        bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False, obdata_animation=False)

        return {'FINISHED'}

class LAZYSUITE_OT_clearparents(bpy.types.Operator):
    
    bl_label = "Clear parents (Keep T.)"
    bl_idname = "lazysuite.clearparents"
    bl_description = "Break the bonds between the selected objects and their parents, keeping transforms."
    def execute(self, context):
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        return {'FINISHED'}
    
# --------------------------------------------------------------------------------

class LAZYSUITE_OT_createempty(bpy.types.Operator):
    
    bl_label = "Empty (0,0,0)"
    bl_idname = "lazysuite.createempty"
    bl_description = "Create a EMPTY object in 0.0.0 location"
    def execute(self, context):
        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.object.name = "_EMPTY"
        return {'FINISHED'}

class LAZYSUITE_OT_createsuzanne(bpy.types.Operator):
    
    bl_label = "Suzanne (0,0,0)"
    bl_idname = "lazysuite.createsuzanne"
    bl_description = "Create a SUZANNE object in 0.0.0 location"
    def execute(self, context):
        bpy.ops.mesh.primitive_monkey_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        return {'FINISHED'}

class LAZYSUITE_OT_addmodifier_mirror(bpy.types.Operator):
    
    bl_label = "Mirror (X + Clipping)"
    bl_idname = "lazysuite.addmodifier_mirror"
    bl_description = "Add a MIRROR modifier on the X axis, with clipping toggled on"
    def execute(self, context):
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_clip = True
        bpy.context.object.modifiers["Mirror"].show_on_cage = True
        bpy.context.object.modifiers["Mirror"].show_in_editmode = True
        return {'FINISHED'}

class LAZYSUITE_OT_addmodifier_bevel(bpy.types.Operator):
    
    bl_label = "Bevel (Weight)"
    bl_idname = "lazysuite.addmodifier_bevel"
    bl_description = "Add a BEVEL modifier with the weight option toggled on"
    def execute(self, context):
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].limit_method = 'WEIGHT'
        return {'FINISHED'}

class LAZYSUITE_OT_addmodifier_shrinkwrap(bpy.types.Operator):
    bl_label = "Shrinkwrap (Select.)"
    bl_idname = "lazysuite.addmodifier_shrinkwrap"
    bl_description = "Add a SHRINKWARP modifier on the ACTIVE object with the PASSIVE selected object as a target, with a DISPLACEMENT modifier"
    def execute(self, context):
        bpy.ops.object.modifier_add(type='SHRINKWRAP')
        bpy.context.object.modifiers["Shrinkwrap"].target = bpy.context.selected_objects[0]
        bpy.ops.object.modifier_add(type='DISPLACE')
        bpy.context.object.modifiers["Displace"].strength = 0.01
        bpy.context.object.modifiers["Displace"].show_on_cage = True
        bpy.context.object.modifiers["Displace"].show_in_editmode = True
        return {'FINISHED'}

class LAZYSUITE_OT_prepsculpt(bpy.types.Operator):
    
    bl_label = "Autoremesh"
    bl_idname = "lazysuite.prepsculpt"
    bl_description = "Apply transforms, origin, and modifiers, join objects then add a remesh modifier with a given amount. REMESH MODIFIER NOT APPLIED"
    def execute(self, context):
        scene = context.scene
        sel_obj = bpy.context.selected_objects
        for i, val in enumerate(sel_obj):
            bpy.ops.object.convert(target='MESH')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.join()
        bpy.ops.object.modifier_add(type='REMESH')
        bpy.context.object.modifiers["Remesh"].voxel_size = scene.prepsculpt_remesh

        return {'FINISHED'}
    
# --------------------------------------------------------------------------------

class LAZYSUITE_OT_addchecker_512(bpy.types.Operator):
    
    bl_label = "512"
    bl_idname = "lazysuite.addchecker_512"
    def execute(self, context):
        bpy.ops.object.material_slot_remove()
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        
        img = bpy.ops.image.new(name='T_checker_512', width=512, height=512, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='COLOR_GRID', float=False, use_stereo_3d=False, tiled=False)
        
        mat = bpy.data.materials.new(name="MAT_checker_512")
        mat.use_nodes = True
        
        shd = mat.node_tree.nodes["Principled BSDF"]
        texImg = mat.node_tree.nodes.new('ShaderNodeTexImage')
        texImg.image = bpy.data.images.get("T_checker_512")
        mat.node_tree.links.new(texImg.outputs[0], shd.inputs[0])

        
        msh = bpy.context.active_object
        msh.data.materials.append(mat)
        
        bpy.context.space_data.shading.color_type = 'TEXTURE'

        return {'FINISHED'}
    
class LAZYSUITE_OT_addchecker_1024(bpy.types.Operator):
    
    bl_label = "1024"
    bl_idname = "lazysuite.addchecker_1024"
    def execute(self, context):
        bpy.ops.object.material_slot_remove()
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        
        img = bpy.ops.image.new(name='T_checker_1024', width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='COLOR_GRID', float=False, use_stereo_3d=False, tiled=False)
        
        mat = bpy.data.materials.new(name="MAT_checker_1024")
        mat.use_nodes = True
        
        shd = mat.node_tree.nodes["Principled BSDF"]
        texImg = mat.node_tree.nodes.new('ShaderNodeTexImage')
        texImg.image = bpy.data.images.get("T_checker_1024")
        mat.node_tree.links.new(texImg.outputs[0], shd.inputs[0])

        
        msh = bpy.context.active_object
        msh.data.materials.append(mat)
        
        bpy.context.space_data.shading.color_type = 'TEXTURE'

        return {'FINISHED'}
    
class LAZYSUITE_OT_addchecker_2048(bpy.types.Operator):
    bl_label = "2048"
    bl_idname = "lazysuite.addchecker_2048"
    def execute(self, context):
        bpy.ops.object.material_slot_remove()
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        
        img = bpy.ops.image.new(name='T_checker_2048', width=2048, height=2048, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='COLOR_GRID', float=False, use_stereo_3d=False, tiled=False)
        
        mat = bpy.data.materials.new(name="MAT_checker_2048")
        mat.use_nodes = True
        
        shd = mat.node_tree.nodes["Principled BSDF"]
        texImg = mat.node_tree.nodes.new('ShaderNodeTexImage')
        texImg.image = bpy.data.images.get("T_checker_2048")
        mat.node_tree.links.new(texImg.outputs[0], shd.inputs[0])

        
        msh = bpy.context.active_object
        msh.data.materials.append(mat)
        
        bpy.context.space_data.shading.color_type = 'TEXTURE'

        return {'FINISHED'}

class LAZYSUITE_OT_addchecker_4096(bpy.types.Operator):
    bl_label = "4096"
    bl_idname = "lazysuite.addchecker_4096"
    def execute(self, context):
        bpy.ops.object.material_slot_remove()
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        
        img = bpy.ops.image.new(name='T_checker_4096', width=4096, height=4096, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='COLOR_GRID', float=False, use_stereo_3d=False, tiled=False)
        
        mat = bpy.data.materials.new(name="MAT_checker_4096")
        mat.use_nodes = True
        
        shd = mat.node_tree.nodes["Principled BSDF"]
        texImg = mat.node_tree.nodes.new('ShaderNodeTexImage')
        texImg.image = bpy.data.images.get("T_checker_4096")
        mat.node_tree.links.new(texImg.outputs[0], shd.inputs[0])

        
        msh = bpy.context.active_object
        msh.data.materials.append(mat)
        
        bpy.context.space_data.shading.color_type = 'TEXTURE'

        return {'FINISHED'}



# --------------------------------------------------------------------------------

class LAZYSUITE_OT_applyname_geo(bpy.types.Operator):
    
    bl_label = "Mesh"
    bl_idname = "lazysuite.applyname_geo"
    def execute(self, context):
        scene = context.scene
        if bpy.context.object.type == 'MESH':
            cur_name = str(bpy.context.object.name)
            if cur_name[:len(str(scene.newName_geo))] != scene.newName_geo:
                bpy.context.object.name = str(scene.newName_geo + bpy.context.object.name)
        else:
            pass
        return {'FINISHED'}
    
class LAZYSUITE_OT_applyname_rig(bpy.types.Operator):
    
    bl_label = "Rig"
    bl_idname = "lazysuite.applyname_rig"

    def execute(self, context):
        scene = context.scene
        if bpy.context.object.type == 'ARMATURE':
            cur_name = str(bpy.context.object.name)
            if cur_name[:len(str(scene.newName_rig))] != scene.newName_rig:
                bpy.context.object.name = str(scene.newName_rig + bpy.context.object.name)
        else:
            pass
        return {'FINISHED'}

class LAZYSUITE_OT_applyname_empty(bpy.types.Operator):
    
    bl_label = "Empty"
    bl_idname = "lazysuite.applyname_empty"

    def execute(self, context):
        scene = context.scene
        if bpy.context.object.type == 'EMPTY':
            cur_name = str(bpy.context.object.name)
            if cur_name[:len(str(scene.newName_empty))] != scene.newName_empty:
                bpy.context.object.name = str(scene.newName_empty + bpy.context.object.name)
        else:
            pass
        return {'FINISHED'}

class LAZYSUITE_OT_applyname_curve(bpy.types.Operator):
    
    bl_label = "Curve"
    bl_idname = "lazysuite.applyname_curve"

    def execute(self, context):
        scene = context.scene
        if bpy.context.object.type == 'CURVE':
            cur_name = str(bpy.context.object.name)
            if cur_name[:len(str(scene.newName_curve))] != scene.newName_curve:
                bpy.context.object.name = str(scene.newName_curve + bpy.context.object.name)
        else:
            pass
        return {'FINISHED'}

class LAZYSUITE_OT_applyname_bool(bpy.types.Operator):
    
    bl_label = "Bool"
    bl_idname = "lazysuite.applyname_bool"

    def execute(self, context):
        scene = context.scene
        if bpy.context.object.type == 'MESH':
            cur_name = str(bpy.context.object.name)
            if cur_name[:len(str(scene.newName_bool))] != scene.newName_bool:
                bpy.context.object.name = str(scene.newName_bool + bpy.context.object.name)
        else:
            pass
        return {'FINISHED'}
    
# -------------------------------------------------------------------------------------
    
classes = [LAZYSUITE_PT_main_panel, LAZYSUITE_PT_panelA, LAZYSUITE_PT_panelB, LAZYSUITE_PT_panelC, LAZYSUITE_PT_panelD, LAZYSUITE_OT_applyrotation_rig, LAZYSUITE_OT_applytransform, LAZYSUITE_OT_cleartransform, LAZYSUITE_OT_fixnormals, LAZYSUITE_OT_origintoselect, LAZYSUITE_OT_makesingle,
LAZYSUITE_OT_clearparents, LAZYSUITE_OT_createempty, LAZYSUITE_OT_createsuzanne, LAZYSUITE_OT_addmodifier_mirror, LAZYSUITE_OT_addmodifier_bevel, LAZYSUITE_OT_addmodifier_shrinkwrap,
LAZYSUITE_OT_prepsculpt, LAZYSUITE_OT_addchecker_512, LAZYSUITE_OT_addchecker_1024, LAZYSUITE_OT_addchecker_2048, LAZYSUITE_OT_addchecker_4096, LAZYSUITE_OT_applyname_geo, LAZYSUITE_OT_applyname_rig, LAZYSUITE_OT_applyname_empty, LAZYSUITE_OT_applyname_curve, LAZYSUITE_OT_applyname_bool]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.newName_geo = bpy.props.StringProperty(name='', default="GEO_")
    bpy.types.Scene.newName_rig = bpy.props.StringProperty(name='', default="RIG_")
    bpy.types.Scene.newName_empty = bpy.props.StringProperty(name='', default="EMPT_")
    bpy.types.Scene.newName_curve = bpy.props.StringProperty(name='', default="CURV_")
    bpy.types.Scene.newName_bool = bpy.props.StringProperty(name='', default="BOOL_")
    bpy.types.Scene.prepsculpt_remesh = bpy.props.FloatProperty(name='', default= 0.01, min = 0.0001, max = 0.5)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
