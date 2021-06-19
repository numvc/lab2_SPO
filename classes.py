from ctypes import *


class ArrayCharPointer(Structure):
    _fields_ = [
        ("char_pointer", c_char_p)
    ]


class ArrayDouble(Structure):
    _fields_ = [
        ("double_elem", c_double)
    ]


class Output(Structure):
    _fields_ = [
        ("d_name", c_char_p),
        ("size", c_double),
        ("information", c_char_p)
    ]


class Mode(Structure):
    _fields_ = [("mode", c_char),
                ("path", c_char)]


class Operation(Structure):
    _fields_ = [("command", c_char),
                ("first_argument", c_char),
                ("second_argument", c_char)
                ]


class ArrayUINT32(Structure):
    _fields_ = [("uint32_elem", c_uint32)]


class ArrayChar(Structure):
    _fields_ = [("char_elem", c_char)]


class ArrayUINT8(Structure):
    _fields_ = [("uint8_elem", c_uint8)]


class SuperBlock(Structure):
    _fields_ = [
        ("s_inodes_count", c_uint32),
        ("s_blocks_count", c_uint32),
        ("s_r_blocks_count", c_uint32),
        ("s_free_blocks_count", c_uint32),
        ("s_free_inodes_count", c_uint32),
        ("s_first_data_block", c_uint32),
        ("s_log_block_size", c_uint32),
        ("s_log_frag_size", c_int32),
        ("s_blocks_per_group", c_uint32),
        ("s_frags_per_group", c_uint32),
        ("s_inodes_per_group", c_uint32),
        ("s_mtime", c_uint32),
        ("s_wtime", c_uint32),
        ("s_mnt_count", c_uint16),
        ("s_max_mnt_count", c_int16),
        ("s_magic", c_uint16),
        ("s_state", c_uint16),
        ("s_errors", c_uint16),
        ("s_minor_rev_level", c_uint16),
        ("s_lastcheck", c_uint32),
        ("s_checkinterval", c_uint32),
        ("s_creator_os", c_uint32),
        ("s_rev_level", c_uint32),
        ("s_def_resuid", c_uint16),
        ("s_def_resgid", c_uint16),
        ("s_first_ino", c_uint32),
        ("s_inode_size", c_uint16),
        ("s_block_group_nr", c_uint16),
        ("s_feature_compat", c_uint32),
        ("s_feature_incompat", c_uint32),
        ("s_feature_ro_compat", c_uint32),
        ("s_uuid", ArrayUINT8 * 16),
        ("s_volume_name", ArrayChar * 16),
        ("s_last_mounted", ArrayChar * 64),
        ("s_algorithm_usage_bitmap", c_uint32),
        ("s_journal_uuid", ArrayUINT8 * 8),
        ("s_journal_inum", c_uint32),
        ("s_journal_dev", c_uint32),
        ("s_last_orphan", c_uint32),
        ("s_hash_seed", ArrayUINT32 * 4),
        ("s_def_hash_version", c_uint8),
        ("s_reserved_char_pad", c_uint8),
        ("s_reserved_word_pad", c_uint16),
        ("s_default_mount_opts", c_uint32),
        ("s_first_meta_bg", c_uint32),
        ("s_reserved", ArrayUINT32 * 190),
    ]


class GroupDesc(Structure):
    _fields_ = [
        ("bg_block_bitmap", c_uint32),
        ("bg_inode_bitmap", c_uint32),
        ("bg_inode_table", c_uint32),
        ("bg_free_blocks_count", c_uint16),
        ("bg_free_inodes_count", c_uint16),
        ("bg_used_dirs_count", c_uint16),
        ("bg_pad", c_uint16),
        ("bg_reserved", ArrayUINT32 * 3)
    ]


class FsState(Structure):
    _fields_ = [("device_path", ArrayChar * 4096),
                ("current_path", ArrayChar * 4096),
                ("current_inode", c_uint),
                ("block_size", c_int),
                ("ext_super_block", POINTER(SuperBlock)),
                ("ext_group_desc", POINTER(GroupDesc))
                ]
