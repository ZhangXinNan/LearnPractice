Ç!
þÐ
:
Add
x"T
y"T
z"T"
Ttype:
2	
x
Assign
ref"T

value"T

output_ref"T"	
Ttype"
validate_shapebool("
use_lockingbool(
8
Const
output"dtype"
valuetensor"
dtypetype
.
Identity

input"T
output"T"	
Ttype
e
MergeV2Checkpoints
checkpoint_prefixes
destination_prefix"
delete_old_dirsbool(
=
Mul
x"T
y"T
z"T"
Ttype:
2	

NoOp
M
Pack
values"T*N
output"T"
Nint(0"	
Ttype"
axisint 
C
Placeholder
output"dtype"
dtypetype"
shapeshape:
o
	RestoreV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0
l
SaveV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0
H
ShardedFilename
basename	
shard

num_shards
filename
N

StringJoin
inputs*N

output"
Nint(0"
	separatorstring 
s

VariableV2
ref"dtype"
shapeshape"
dtypetype"
	containerstring "
shared_namestring "cpu_server_1*1.5.02v1.5.0-0-g37aa430d84ý
F
xPlaceholder*
dtype0*
shape:*
_output_shapes
:
F
yPlaceholder*
dtype0*
shape:*
_output_shapes
:
Q
b/initial_valueConst*
dtype0*
value	B :*
_output_shapes
: 
e
b
VariableV2*
dtype0*
shape: *
	container *
shared_name *
_output_shapes
: 

b/AssignAssignbb/initial_value*
validate_shape(*
_class

loc:@b*
use_locking(*
T0*
_output_shapes
: 
L
b/readIdentityb*
_class

loc:@b*
T0*
_output_shapes
: 
3
MulMulxy*
T0*
_output_shapes
:
B
op_to_storeAddMulb/read*
T0*
_output_shapes
:

initNoOp	^b/Assign
P

save/ConstConst*
dtype0*
valueB Bmodel*
_output_shapes
: 

save/StringJoin/inputs_1Const*
dtype0*<
value3B1 B+_temp_bc8b7a0e5f0546a3bede6efe64308079/part*
_output_shapes
: 
u
save/StringJoin
StringJoin
save/Constsave/StringJoin/inputs_1*
_output_shapes
: *
	separator *
N
Q
save/num_shardsConst*
dtype0*
value	B :*
_output_shapes
: 
k
save/ShardedFilename/shardConst"/device:CPU:0*
dtype0*
value	B : *
_output_shapes
: 

save/ShardedFilenameShardedFilenamesave/StringJoinsave/ShardedFilename/shardsave/num_shards"/device:CPU:0*
_output_shapes
: 
q
save/SaveV2/tensor_namesConst"/device:CPU:0*
dtype0*
valueBBb*
_output_shapes
:
t
save/SaveV2/shape_and_slicesConst"/device:CPU:0*
dtype0*
valueB
B *
_output_shapes
:

save/SaveV2SaveV2save/ShardedFilenamesave/SaveV2/tensor_namessave/SaveV2/shape_and_slicesb"/device:CPU:0*
dtypes
2
 
save/control_dependencyIdentitysave/ShardedFilename^save/SaveV2"/device:CPU:0*'
_class
loc:@save/ShardedFilename*
T0*
_output_shapes
: 
¬
+save/MergeV2Checkpoints/checkpoint_prefixesPacksave/ShardedFilename^save/control_dependency"/device:CPU:0*
N*

axis *
T0*
_output_shapes
:

save/MergeV2CheckpointsMergeV2Checkpoints+save/MergeV2Checkpoints/checkpoint_prefixes
save/Const"/device:CPU:0*
delete_old_dirs(

save/IdentityIdentity
save/Const^save/control_dependency^save/MergeV2Checkpoints"/device:CPU:0*
T0*
_output_shapes
: 
e
save/RestoreV2/tensor_namesConst*
dtype0*
valueBBb*
_output_shapes
:
h
save/RestoreV2/shape_and_slicesConst*
dtype0*
valueB
B *
_output_shapes
:

save/RestoreV2	RestoreV2
save/Constsave/RestoreV2/tensor_namessave/RestoreV2/shape_and_slices*
dtypes
2*
_output_shapes
:

save/AssignAssignbsave/RestoreV2*
validate_shape(*
_class

loc:@b*
use_locking(*
T0*
_output_shapes
: 
(
save/restore_shardNoOp^save/Assign
-
save/restore_allNoOp^save/restore_shard"<
save/Const:0save/Identity:0save/restore_all (5 @F8"=
	variables0.
,
b:0b/Assignb/read:02b/initial_value:0"G
trainable_variables0.
,
b:0b/Assignb/read:02b/initial_value:0