import time 
my_list = ["Nemo"]
my_list_2 = ["Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98","Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Name_0", "Name_1", "Name_2", "Name_3", "Name_4", "Name_5", "Name_6", "Name_7", "Name_8", "Name_9", "Name_10", "Name_11", "Name_12", "Name_13", "Name_14", "Name_15", "Name_16", "Name_17", "Name_18", "Name_19", "Name_20", "Name_21", "Name_22", "Name_23", "Name_24", "Name_25", "Name_26", "Name_27", "Name_28", "Name_29", "Name_30", "Name_31", "Name_32", "Name_33", "Name_34", "Name_35", "Name_36", "Name_37", "Name_38", "Name_39", "Name_40", "Name_41", "Name_42", "Name_43", "Name_44", "Name_45", "Name_46", "Name_47", "Name_48", "Name_49", "Name_50", "Name_51", "Name_52", "Name_53", "Name_54", "Name_55", "Name_56", "Name_57", "Name_58", "Name_59", "Name_60", "Name_61", "Name_62", "Name_63", "Name_64", "Name_65", "Name_66", "Name_67", "Name_68", "Name_69", "Name_70", "Name_71", "Name_72", "Name_73", "Name_74", "Name_75", "Name_76", "Name_77", "Name_78", "Name_79", "Name_80", "Name_81", "Name_82", "Name_83", "Name_84", "Name_85", "Name_86", "Name_87", "Name_88", "Name_89", "Name_90", "Name_91", "Name_92", "Name_93", "Name_94", "Name_95", "Name_96", "Name_97", "Name_98", "Nemo"]

def findNemo(array):
    start_time = time.perf_counter()  # Start time inside the function

    for i in range(len(array)): 
        if array[i] == "Nemo":
            print("Found Nemo! :)")
            end_time = time.perf_counter()  # End time after finding Nemo
            execution_time = end_time - start_time
            print(f"Execution time: {execution_time} seconds")
            return
    print("Nemo Not Found. :(")  
    end_time = time.perf_counter()  
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

findNemo(my_list)
findNemo(my_list_2)