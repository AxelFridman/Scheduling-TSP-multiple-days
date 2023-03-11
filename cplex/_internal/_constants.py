# --------------------------------------------------------------------------
# File: _constants.py
# ---------------------------------------------------------------------------
# Licensed Materials - Property of IBM
# 5725-A06 5725-A29 5724-Y48 5724-Y49 5724-Y54 5724-Y55 5655-Y21
# Copyright IBM Corporation 2008, 2022. All Rights Reserved.
#
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with
# IBM Corp.
# ------------------------------------------------------------------------
"""Constants from the CPLEX C Callable Library"""

CPX_FEATURES_H = 1
CPX_STR_PARAM_MAX = 512
CPX_INFBOUND = 1.0E+20
CPX_MINBOUND = 1.0E-13
CPX_PWL_MAXSLOPE = 1.0E+6
CPX_PWL_MINSLOPE = 1.0E-6
CPX_PARAMTYPE_NONE = 0
CPX_PARAMTYPE_INT = 1
CPX_PARAMTYPE_DOUBLE = 2
CPX_PARAMTYPE_STRING = 3
CPX_PARAMTYPE_LONG = 4
CPX_NO_SOLN = 0
CPX_AUTO_SOLN = 0
CPX_BASIC_SOLN = 1
CPX_NONBASIC_SOLN = 2
CPX_PRIMAL_SOLN = 3
CPX_PRECOL_LOW = -1
CPX_PRECOL_UP = -2
CPX_PRECOL_FIX = -3
CPX_PRECOL_AGG = -4
CPX_PRECOL_OTHER = -5
CPX_PREROW_RED = -1
CPX_PREROW_AGG = -2
CPX_PREROW_OTHER = -3
CPX_AUTO = -1
CPX_ON = 1
CPX_OFF = 0
CPX_MAX = -1
CPX_MIN = 1
CPX_DATACHECK_OFF = 0
CPX_DATACHECK_WARN = 1
CPX_DATACHECK_ASSIST = 2
CPX_PPRIIND_PARTIAL = -1
CPX_PPRIIND_AUTO = 0
CPX_PPRIIND_DEVEX = 1
CPX_PPRIIND_STEEP = 2
CPX_PPRIIND_STEEPQSTART = 3
CPX_PPRIIND_FULL = 4
CPX_DPRIIND_AUTO = 0
CPX_DPRIIND_FULL = 1
CPX_DPRIIND_STEEP = 2
CPX_DPRIIND_FULLSTEEP = 3
CPX_DPRIIND_STEEPQSTART = 4
CPX_DPRIIND_DEVEX = 5
CPX_PARALLEL_DETERMINISTIC = 1
CPX_PARALLEL_AUTO = 0
CPX_PARALLEL_OPPORTUNISTIC = -1
CPX_WRITELEVEL_AUTO = 0
CPX_WRITELEVEL_ALLVARS = 1
CPX_WRITELEVEL_DISCRETEVARS = 2
CPX_WRITELEVEL_NONZEROVARS = 3
CPX_WRITELEVEL_NONZERODISCRETEVARS = 4
CPX_OPTIMALITYTARGET_AUTO = 0
CPX_OPTIMALITYTARGET_OPTIMALCONVEX = 1
CPX_OPTIMALITYTARGET_FIRSTORDER = 2
CPX_OPTIMALITYTARGET_OPTIMALGLOBAL = 3
CPX_ALG_NONE = -1
CPX_ALG_AUTOMATIC = 0
CPX_ALG_PRIMAL = 1
CPX_ALG_DUAL = 2
CPX_ALG_NET = 3
CPX_ALG_BARRIER = 4
CPX_ALG_SIFTING = 5
CPX_ALG_CONCURRENT = 6
CPX_ALG_BAROPT = 7
CPX_ALG_PIVOTIN = 8
CPX_ALG_PIVOTOUT = 9
CPX_ALG_PIVOT = 10
CPX_ALG_FEASOPT = 11
CPX_ALG_MIP = 12
CPX_ALG_BENDERS = 13
CPX_ALG_MULTIOBJ = 14
CPX_ALG_ROBUST = 15
CPX_AT_LOWER = 0
CPX_BASIC = 1
CPX_AT_UPPER = 2
CPX_FREE_SUPER = 3
CPX_NO_VARIABLE = 2100000000
CPX_CONTINUOUS = 'C'
CPX_BINARY = 'B'
CPX_INTEGER = 'I'
CPX_SEMICONT = 'S'
CPX_SEMIINT = 'N'
CPX_PREREDUCE_PRIMALANDDUAL = 3
CPX_PREREDUCE_DUALONLY = 2
CPX_PREREDUCE_PRIMALONLY = 1
CPX_PREREDUCE_NOPRIMALORDUAL = 0
CPX_PREREFORM_ALL = 3
CPX_PREREFORM_INTERFERE_CRUSH = 1
CPX_PREREFORM_INTERFERE_UNCRUSH = 2
CPX_PREREFORM_NONE = 0
CPX_CONFLICT_EXCLUDED = -1
CPX_CONFLICT_POSSIBLE_MEMBER = 0
CPX_CONFLICT_POSSIBLE_LB = 1
CPX_CONFLICT_POSSIBLE_UB = 2
CPX_CONFLICT_MEMBER = 3
CPX_CONFLICT_LB = 4
CPX_CONFLICT_UB = 5
CPX_CONFLICTALG_AUTO = 0
CPX_CONFLICTALG_FAST = 1
CPX_CONFLICTALG_PROPAGATE = 2
CPX_CONFLICTALG_PRESOLVE = 3
CPX_CONFLICTALG_IIS = 4
CPX_CONFLICTALG_LIMITSOLVE = 5
CPX_CONFLICTALG_SOLVE = 6
CPXPROB_LP = 0
CPXPROB_MILP = 1
CPXPROB_FIXEDMILP = 3
CPXPROB_NODELP = 4
CPXPROB_QP = 5
CPXPROB_MIQP = 7
CPXPROB_FIXEDMIQP = 8
CPXPROB_NODEQP = 9
CPXPROB_QCP = 10
CPXPROB_MIQCP = 11
CPXPROB_NODEQCP = 12
CPX_LPREADER_LEGACY = 0
CPX_LPREADER_NEW = 1
CPX_PARAM_ALL_MIN = 1000
CPX_PARAM_ALL_MAX = 6000
CPX_CALLBACK_PRIMAL = 1
CPX_CALLBACK_DUAL = 2
CPX_CALLBACK_NETWORK = 3
CPX_CALLBACK_PRIMAL_CROSSOVER = 4
CPX_CALLBACK_DUAL_CROSSOVER = 5
CPX_CALLBACK_BARRIER = 6
CPX_CALLBACK_PRESOLVE = 7
CPX_CALLBACK_QPBARRIER = 8
CPX_CALLBACK_QPSIMPLEX = 9
CPX_CALLBACK_TUNING = 10
CPX_CALLBACK_INFO_PRIMAL_OBJ = 1
CPX_CALLBACK_INFO_DUAL_OBJ = 2
CPX_CALLBACK_INFO_PRIMAL_INFMEAS = 3
CPX_CALLBACK_INFO_DUAL_INFMEAS = 4
CPX_CALLBACK_INFO_PRIMAL_FEAS = 5
CPX_CALLBACK_INFO_DUAL_FEAS = 6
CPX_CALLBACK_INFO_ITCOUNT = 7
CPX_CALLBACK_INFO_CROSSOVER_PPUSH = 8
CPX_CALLBACK_INFO_CROSSOVER_PEXCH = 9
CPX_CALLBACK_INFO_CROSSOVER_DPUSH = 10
CPX_CALLBACK_INFO_CROSSOVER_DEXCH = 11
CPX_CALLBACK_INFO_CROSSOVER_SBCNT = 12
CPX_CALLBACK_INFO_PRESOLVE_ROWSGONE = 13
CPX_CALLBACK_INFO_PRESOLVE_COLSGONE = 14
CPX_CALLBACK_INFO_PRESOLVE_AGGSUBST = 15
CPX_CALLBACK_INFO_PRESOLVE_COEFFS = 16
CPX_CALLBACK_INFO_USER_PROBLEM = 17
CPX_CALLBACK_INFO_TUNING_PROGRESS = 18
CPX_CALLBACK_INFO_ENDTIME = 19
CPX_CALLBACK_INFO_ITCOUNT_LONG = 20
CPX_CALLBACK_INFO_CROSSOVER_PPUSH_LONG = 21
CPX_CALLBACK_INFO_CROSSOVER_PEXCH_LONG = 22
CPX_CALLBACK_INFO_CROSSOVER_DPUSH_LONG = 23
CPX_CALLBACK_INFO_CROSSOVER_DEXCH_LONG = 24
CPX_CALLBACK_INFO_PRESOLVE_AGGSUBST_LONG = 25
CPX_CALLBACK_INFO_PRESOLVE_COEFFS_LONG = 26
CPX_CALLBACK_INFO_ENDDETTIME = 27
CPX_CALLBACK_INFO_STARTTIME = 28
CPX_CALLBACK_INFO_STARTDETTIME = 29
CPX_TUNE_AVERAGE = 1
CPX_TUNE_MINMAX = 2
CPX_TUNE_ABORT = 1
CPX_TUNE_TILIM = 2
CPX_TUNE_DETTILIM = 3
CPX_FEASOPT_MIN_SUM = 0
CPX_FEASOPT_OPT_SUM = 1
CPX_FEASOPT_MIN_INF = 2
CPX_FEASOPT_OPT_INF = 3
CPX_FEASOPT_MIN_QUAD = 4
CPX_FEASOPT_OPT_QUAD = 5
CPX_BENDERSSTRATEGY_OFF = -1
CPX_BENDERSSTRATEGY_AUTO = 0
CPX_BENDERSSTRATEGY_USER = 1
CPX_BENDERSSTRATEGY_WORKERS = 2
CPX_BENDERSSTRATEGY_FULL = 3
CPX_ANNOTATIONDATA_LONG = 1
CPX_ANNOTATIONDATA_DOUBLE = 2
CPX_ANNOTATIONOBJ_OBJ = 0
CPX_ANNOTATIONOBJ_COL = 1
CPX_ANNOTATIONOBJ_ROW = 2
CPX_ANNOTATIONOBJ_SOS = 3
CPX_ANNOTATIONOBJ_IND = 4
CPX_ANNOTATIONOBJ_QC = 5
CPX_ANNOTATIONOBJ_LAST = 6
CPXIIS_COMPLETE = 1
CPXIIS_PARTIAL = 2
CPXIIS_AT_LOWER = 0
CPXIIS_FIXED = 1
CPXIIS_AT_UPPER = 2
CPX_BARORDER_AUTO = 0
CPX_BARORDER_AMD = 1
CPX_BARORDER_AMF = 2
CPX_BARORDER_ND = 3
CPX_MIPEMPHASIS_BALANCED = 0
CPX_MIPEMPHASIS_FEASIBILITY = 1
CPX_MIPEMPHASIS_OPTIMALITY = 2
CPX_MIPEMPHASIS_BESTBOUND = 3
CPX_MIPEMPHASIS_HIDDENFEAS = 4
CPX_MIPEMPHASIS_HEURISTIC = 5
CPX_TYPE_VAR = '0'
CPX_TYPE_SOS1 = '1'
CPX_TYPE_SOS2 = '2'
CPX_TYPE_USER = 'X'
CPX_TYPE_ANY = 'A'
CPX_VARSEL_MININFEAS = -1
CPX_VARSEL_DEFAULT = 0
CPX_VARSEL_MAXINFEAS = 1
CPX_VARSEL_PSEUDO = 2
CPX_VARSEL_STRONG = 3
CPX_VARSEL_PSEUDOREDUCED = 4
CPX_NODESEL_DFS = 0
CPX_NODESEL_BESTBOUND = 1
CPX_NODESEL_BESTEST = 2
CPX_NODESEL_BESTEST_ALT = 3
CPX_MIPORDER_COST = 1
CPX_MIPORDER_BOUNDS = 2
CPX_MIPORDER_SCALEDCOST = 3
CPX_BRANCH_GLOBAL = 0
CPX_BRANCH_DOWN = -1
CPX_BRANCH_UP = 1
CPX_BRDIR_DOWN = -1
CPX_BRDIR_AUTO = 0
CPX_BRDIR_UP = 1
CPX_CUT_COVER = 0
CPX_CUT_GUBCOVER = 1
CPX_CUT_FLOWCOVER = 2
CPX_CUT_CLIQUE = 3
CPX_CUT_FRAC = 4
CPX_CUT_MIR = 5
CPX_CUT_FLOWPATH = 6
CPX_CUT_DISJ = 7
CPX_CUT_IMPLBD = 8
CPX_CUT_ZEROHALF = 9
CPX_CUT_MCF = 10
CPX_CUT_LOCALCOVER = 11
CPX_CUT_TIGHTEN = 12
CPX_CUT_OBJDISJ = 13
CPX_CUT_LANDP = 14
CPX_CUT_USER = 15
CPX_CUT_TABLE = 16
CPX_CUT_SOLNPOOL = 17
CPX_CUT_LOCALIMPLBD = 18
CPX_CUT_BQP = 19
CPX_CUT_RLT = 20
CPX_CUT_BENDERS = 21
CPX_CUT_NUM_TYPES = 22
CPX_MIPSEARCH_AUTO = 0
CPX_MIPSEARCH_TRADITIONAL = 1
CPX_MIPSEARCH_DYNAMIC = 2
CPX_MIPKAPPA_OFF = -1
CPX_MIPKAPPA_AUTO = 0
CPX_MIPKAPPA_SAMPLE = 1
CPX_MIPKAPPA_FULL = 2
CPX_MIPSTART_AUTO = 0
CPX_MIPSTART_CHECKFEAS = 1
CPX_MIPSTART_SOLVEFIXED = 2
CPX_MIPSTART_SOLVEMIP = 3
CPX_MIPSTART_REPAIR = 4
CPX_MIPSTART_NOCHECK = 5
CPX_CALLBACK_MIP = 101
CPX_CALLBACK_MIP_BRANCH = 102
CPX_CALLBACK_MIP_NODE = 103
CPX_CALLBACK_MIP_HEURISTIC = 104
CPX_CALLBACK_MIP_SOLVE = 105
CPX_CALLBACK_MIP_CUT_LOOP = 106
CPX_CALLBACK_MIP_PROBE = 107
CPX_CALLBACK_MIP_FRACCUT = 108
CPX_CALLBACK_MIP_DISJCUT = 109
CPX_CALLBACK_MIP_FLOWMIR = 110
CPX_CALLBACK_MIP_INCUMBENT_NODESOLN = 111
CPX_CALLBACK_MIP_DELETENODE = 112
CPX_CALLBACK_MIP_BRANCH_NOSOLN = 113
CPX_CALLBACK_MIP_CUT_LAST = 114
CPX_CALLBACK_MIP_CUT_FEAS = 115
CPX_CALLBACK_MIP_CUT_UNBD = 116
CPX_CALLBACK_MIP_INCUMBENT_HEURSOLN = 117
CPX_CALLBACK_MIP_INCUMBENT_USERSOLN = 118
CPX_CALLBACK_MIP_INCUMBENT_MIPSTART = 119
CPX_CALLBACK_INFO_BEST_INTEGER = 101
CPX_CALLBACK_INFO_BEST_REMAINING = 102
CPX_CALLBACK_INFO_NODE_COUNT = 103
CPX_CALLBACK_INFO_NODES_LEFT = 104
CPX_CALLBACK_INFO_MIP_ITERATIONS = 105
CPX_CALLBACK_INFO_CUTOFF = 106
CPX_CALLBACK_INFO_CLIQUE_COUNT = 107
CPX_CALLBACK_INFO_COVER_COUNT = 108
CPX_CALLBACK_INFO_MIP_FEAS = 109
CPX_CALLBACK_INFO_FLOWCOVER_COUNT = 110
CPX_CALLBACK_INFO_GUBCOVER_COUNT = 111
CPX_CALLBACK_INFO_IMPLBD_COUNT = 112
CPX_CALLBACK_INFO_PROBE_PHASE = 113
CPX_CALLBACK_INFO_PROBE_PROGRESS = 114
CPX_CALLBACK_INFO_FRACCUT_COUNT = 115
CPX_CALLBACK_INFO_FRACCUT_PROGRESS = 116
CPX_CALLBACK_INFO_DISJCUT_COUNT = 117
CPX_CALLBACK_INFO_DISJCUT_PROGRESS = 118
CPX_CALLBACK_INFO_FLOWPATH_COUNT = 119
CPX_CALLBACK_INFO_MIRCUT_COUNT = 120
CPX_CALLBACK_INFO_FLOWMIR_PROGRESS = 121
CPX_CALLBACK_INFO_ZEROHALFCUT_COUNT = 122
CPX_CALLBACK_INFO_MY_THREAD_NUM = 123
CPX_CALLBACK_INFO_USER_THREADS = 124
CPX_CALLBACK_INFO_MIP_REL_GAP = 125
CPX_CALLBACK_INFO_MCFCUT_COUNT = 126
CPX_CALLBACK_INFO_KAPPA_STABLE = 127
CPX_CALLBACK_INFO_KAPPA_SUSPICIOUS = 128
CPX_CALLBACK_INFO_KAPPA_UNSTABLE = 129
CPX_CALLBACK_INFO_KAPPA_ILLPOSED = 130
CPX_CALLBACK_INFO_KAPPA_MAX = 131
CPX_CALLBACK_INFO_KAPPA_ATTENTION = 132
CPX_CALLBACK_INFO_LANDPCUT_COUNT = 133
CPX_CALLBACK_INFO_USERCUT_COUNT = 134
CPX_CALLBACK_INFO_TABLECUT_COUNT = 135
CPX_CALLBACK_INFO_SOLNPOOLCUT_COUNT = 136
CPX_CALLBACK_INFO_BENDERS_COUNT = 137
CPX_CALLBACK_INFO_NODE_COUNT_LONG = 140
CPX_CALLBACK_INFO_NODES_LEFT_LONG = 141
CPX_CALLBACK_INFO_MIP_ITERATIONS_LONG = 142
CPX_CALLBACK_INFO_LAZY_SOURCE = 143
CPX_CALLBACK_INFO_NODE_SIINF = 201
CPX_CALLBACK_INFO_NODE_NIINF = 202
CPX_CALLBACK_INFO_NODE_ESTIMATE = 203
CPX_CALLBACK_INFO_NODE_DEPTH = 204
CPX_CALLBACK_INFO_NODE_OBJVAL = 205
CPX_CALLBACK_INFO_NODE_TYPE = 206
CPX_CALLBACK_INFO_NODE_VAR = 207
CPX_CALLBACK_INFO_NODE_SOS = 208
CPX_CALLBACK_INFO_NODE_SEQNUM = 209
CPX_CALLBACK_INFO_NODE_USERHANDLE = 210
CPX_CALLBACK_INFO_NODE_NODENUM = 211
CPX_CALLBACK_INFO_NODE_SEQNUM_LONG = 220
CPX_CALLBACK_INFO_NODE_NODENUM_LONG = 221
CPX_CALLBACK_INFO_NODE_DEPTH_LONG = 222
CPX_CALLBACK_INFO_SOS_TYPE = 240
CPX_CALLBACK_INFO_SOS_SIZE = 241
CPX_CALLBACK_INFO_SOS_IS_FEASIBLE = 242
CPX_CALLBACK_INFO_SOS_MEMBER_INDEX = 244
CPX_CALLBACK_INFO_SOS_MEMBER_REFVAL = 246
CPX_CALLBACK_INFO_SOS_NUM = 247
CPX_CALLBACK_INFO_IC_NUM = 260
CPX_CALLBACK_INFO_IC_IMPLYING_VAR = 261
CPX_CALLBACK_INFO_IC_IMPLIED_VAR = 262
CPX_CALLBACK_INFO_IC_SENSE = 263
CPX_CALLBACK_INFO_IC_COMPL = 264
CPX_CALLBACK_INFO_IC_RHS = 265
CPX_CALLBACK_INFO_IC_IS_FEASIBLE = 266
CPX_INCUMBENT_ID = -1
CPX_CALLBACK_DEFAULT = 0
CPX_CALLBACK_FAIL = 1
CPX_CALLBACK_SET = 2
CPX_CALLBACK_ABORT_CUT_LOOP = 3
CPX_USECUT_FORCE = 0
CPX_USECUT_PURGE = 1
CPX_USECUT_FILTER = 2
CPX_INTEGER_FEASIBLE = 0
CPX_INTEGER_INFEASIBLE = 1
CPX_IMPLIED_INTEGER_FEASIBLE = 2
CPX_CON_LOWER_BOUND = 1
CPX_CON_UPPER_BOUND = 2
CPX_CON_LINEAR = 3
CPX_CON_QUADRATIC = 4
CPX_CON_SOS = 5
CPX_CON_INDICATOR = 6
CPX_CON_PWL = 7
CPX_CON_ABS = 7
CPX_CON_MINEXPR = 8
CPX_CON_MAXEXPR = 9
CPX_CON_LAST_CONTYPE = 10
CPX_INDICATOR_IF = 1
CPX_INDICATOR_ONLYIF = 2
CPX_INDICATOR_IFANDONLYIF = 3
CPXNET_NO_DISPLAY_OBJECTIVE = 0
CPXNET_TRUE_OBJECTIVE = 1
CPXNET_PENALIZED_OBJECTIVE = 2
CPXNET_PRICE_AUTO = 0
CPXNET_PRICE_PARTIAL = 1
CPXNET_PRICE_MULT_PART = 2
CPXNET_PRICE_SORT_MULT_PART = 3
CPX_NETFIND_PURE = 1
CPX_NETFIND_REFLECT = 2
CPX_NETFIND_SCALE = 3
CPX_QCPDUALS_NO = 0
CPX_QCPDUALS_IFPOSSIBLE = 1
CPX_QCPDUALS_FORCE = 2
CPX_BENDERS_ANNOTATION = "cpxBendersPartition"
CPX_BENDERS_MASTERVALUE = 0
CPX_BIGINT = 2100000000
CPX_BIGLONG = 9223372036800000000
CPX_CALLBACKCONTEXT_BRANCHING = 0x0080
CPX_CALLBACKCONTEXT_CANDIDATE = 0x0020
CPX_CALLBACKCONTEXT_GLOBAL_PROGRESS = 0x0010
CPX_CALLBACKCONTEXT_LOCAL_PROGRESS = 0x0008
CPX_CALLBACKCONTEXT_RELAXATION = 0x0040
CPX_CALLBACKCONTEXT_THREAD_DOWN = 0x0004
CPX_CALLBACKCONTEXT_THREAD_UP = 0x0002
CPX_DUAL_OBJ = 41
CPX_EXACT_KAPPA = 51
CPX_KAPPA = 39
CPX_KAPPA_ATTENTION = 57
CPX_KAPPA_ILLPOSED = 55
CPX_KAPPA_MAX = 56
CPX_KAPPA_STABLE = 52
CPX_KAPPA_SUSPICIOUS = 53
CPX_KAPPA_UNSTABLE = 54
CPX_LAZYCONSTRAINTCALLBACK_HEUR = CPX_CALLBACK_MIP_INCUMBENT_HEURSOLN
CPX_LAZYCONSTRAINTCALLBACK_MIPSTART = CPX_CALLBACK_MIP_INCUMBENT_MIPSTART
CPX_LAZYCONSTRAINTCALLBACK_NODE = CPX_CALLBACK_MIP_INCUMBENT_NODESOLN
CPX_LAZYCONSTRAINTCALLBACK_USER = CPX_CALLBACK_MIP_INCUMBENT_USERSOLN
CPX_MAX_COMP_SLACK = 19
CPX_MAX_DUAL_INFEAS = 5
CPX_MAX_DUAL_RESIDUAL = 15
CPX_MAX_INDSLACK_INFEAS = 49
CPX_MAX_INT_INFEAS = 9
CPX_MAX_PI = 25
CPX_MAX_PRIMAL_INFEAS = 1
CPX_MAX_PRIMAL_RESIDUAL = 11
CPX_MAX_PWLSLACK_INFEAS = 58
CPX_MAX_QCPRIMAL_RESIDUAL = 43
CPX_MAX_QCSLACK = 47
CPX_MAX_QCSLACK_INFEAS = 45
CPX_MAX_RED_COST = 29
CPX_MAX_SCALED_DUAL_INFEAS = 6
CPX_MAX_SCALED_DUAL_RESIDUAL = 16
CPX_MAX_SCALED_PI = 26
CPX_MAX_SCALED_PRIMAL_INFEAS = 2
CPX_MAX_SCALED_PRIMAL_RESIDUAL = 12
CPX_MAX_SCALED_RED_COST = 30
CPX_MAX_SCALED_SLACK = 28
CPX_MAX_SCALED_X = 24
CPX_MAX_SLACK = 27
CPX_MAX_X = 23
CPX_MULTIOBJ_BARITCNT = 4
CPX_MULTIOBJ_BESTOBJVAL = 15
CPX_MULTIOBJ_BLEND = 20
CPX_MULTIOBJ_DEGCNT = 7
CPX_MULTIOBJ_DETTIME = 3
CPX_MULTIOBJ_DEXCH = 13
CPX_MULTIOBJ_DFEAS = 22
CPX_MULTIOBJ_DPUSH = 12
CPX_MULTIOBJ_ERROR = 0
CPX_MULTIOBJ_ITCNT = 8
CPX_MULTIOBJ_METHOD = 18
CPX_MULTIOBJ_NODECNT = 16
CPX_MULTIOBJ_NODELEFTCNT = 19
CPX_MULTIOBJ_OBJVAL = 14
CPX_MULTIOBJ_PEXCH = 11
CPX_MULTIOBJ_PFEAS = 21
CPX_MULTIOBJ_PHASE1CNT = 9
CPX_MULTIOBJ_PPUSH = 10
CPX_MULTIOBJ_PRIORITY = 17
CPX_MULTIOBJ_SIFTITCNT = 5
CPX_MULTIOBJ_SIFTPHASE1CNT = 6
CPX_MULTIOBJ_STATUS = 1
CPX_MULTIOBJ_TIME = 2
CPX_NO_ABSTOL_CHANGE = float('nan')
CPX_NO_OFFSET_CHANGE = float('nan')
CPX_NO_PRIORITY_CHANGE = -1
CPX_NO_RELTOL_CHANGE = float('nan')
CPX_NO_WEIGHT_CHANGE = float('nan')
CPX_OBJ_GAP = 40
CPX_PRIMAL_OBJ = 42
CPX_RELAXATION_FLAG_NOSOLVE = 0x0001
CPX_SOLNPOOL_DIV = 2
CPX_SOLNPOOL_FIFO = 0
CPX_SOLNPOOL_FILTER_DIVERSITY = 1
CPX_SOLNPOOL_FILTER_RANGE = 2
CPX_SOLNPOOL_OBJ = 1
CPX_STAT_ABORT_DETTIME_LIM = 25
CPX_STAT_ABORT_DUAL_OBJ_LIM = 22
CPX_STAT_ABORT_IT_LIM = 10
CPX_STAT_ABORT_OBJ_LIM = 12
CPX_STAT_ABORT_PRIM_OBJ_LIM = 21
CPX_STAT_ABORT_TIME_LIM = 11
CPX_STAT_ABORT_USER = 13
CPX_STAT_BENDERS_NUM_BEST = 41
CPX_STAT_CONFLICT_ABORT_CONTRADICTION = 32
CPX_STAT_CONFLICT_ABORT_DETTIME_LIM = 39
CPX_STAT_CONFLICT_ABORT_IT_LIM = 34
CPX_STAT_CONFLICT_ABORT_MEM_LIM = 37
CPX_STAT_CONFLICT_ABORT_NODE_LIM = 35
CPX_STAT_CONFLICT_ABORT_OBJ_LIM = 36
CPX_STAT_CONFLICT_ABORT_TIME_LIM = 33
CPX_STAT_CONFLICT_ABORT_USER = 38
CPX_STAT_CONFLICT_FEASIBLE = 30
CPX_STAT_CONFLICT_MINIMAL = 31
CPX_STAT_FEASIBLE = 23
CPX_STAT_FEASIBLE_RELAXED_INF = 16
CPX_STAT_FEASIBLE_RELAXED_QUAD = 18
CPX_STAT_FEASIBLE_RELAXED_SUM = 14
CPX_STAT_FIRSTORDER = 24
CPX_STAT_INFEASIBLE = 3
CPX_STAT_INForUNBD = 4
CPX_STAT_MULTIOBJ_INFEASIBLE = 302
CPX_STAT_MULTIOBJ_INForUNBD = 303
CPX_STAT_MULTIOBJ_NON_OPTIMAL = 305
CPX_STAT_MULTIOBJ_OPTIMAL = 301
CPX_STAT_MULTIOBJ_STOPPED = 306
CPX_STAT_MULTIOBJ_UNBOUNDED = 304
CPX_STAT_NUM_BEST = 6
CPX_STAT_OPTIMAL = 1
CPX_STAT_OPTIMAL_FACE_UNBOUNDED = 20
CPX_STAT_OPTIMAL_INFEAS = 5
CPX_STAT_OPTIMAL_RELAXED_INF = 17
CPX_STAT_OPTIMAL_RELAXED_QUAD = 19
CPX_STAT_OPTIMAL_RELAXED_SUM = 15
CPX_STAT_UNBOUNDED = 2
CPX_STAT_UNKNOWN = 0
CPX_SUM_COMP_SLACK = 21
CPX_SUM_DUAL_INFEAS = 7
CPX_SUM_DUAL_RESIDUAL = 17
CPX_SUM_INDSLACK_INFEAS = 50
CPX_SUM_INT_INFEAS = 10
CPX_SUM_PI = 33
CPX_SUM_PRIMAL_INFEAS = 3
CPX_SUM_PRIMAL_RESIDUAL = 13
CPX_SUM_PWLSLACK_INFEAS = 59
CPX_SUM_QCPRIMAL_RESIDUAL = 44
CPX_SUM_QCSLACK = 48
CPX_SUM_QCSLACK_INFEAS = 46
CPX_SUM_RED_COST = 37
CPX_SUM_SCALED_DUAL_INFEAS = 8
CPX_SUM_SCALED_DUAL_RESIDUAL = 18
CPX_SUM_SCALED_PI = 34
CPX_SUM_SCALED_PRIMAL_INFEAS = 4
CPX_SUM_SCALED_PRIMAL_RESIDUAL = 14
CPX_SUM_SCALED_RED_COST = 38
CPX_SUM_SCALED_SLACK = 36
CPX_SUM_SCALED_X = 32
CPX_SUM_SLACK = 35
CPX_SUM_X = 31
CPXMI_BIGM_COEF = 1040
CPXMI_BIGM_TO_IND = 1041
CPXMI_BIGM_VARBOUND = 1042
CPXMI_CANCEL_TOL = 1045
CPXMI_EPGAP_LARGE = 1038
CPXMI_EPGAP_OBJOFFSET = 1037
CPXMI_FEAS_TOL = 1043
CPXMI_FRACTION_SCALING = 1047
CPXMI_IND_NZ_LARGE_NUM = 1019
CPXMI_IND_NZ_SMALL_NUM = 1020
CPXMI_IND_RHS_LARGE_NUM = 1021
CPXMI_IND_RHS_SMALL_NUM = 1022
CPXMI_KAPPA_ILLPOSED = 1035
CPXMI_KAPPA_SUSPICIOUS = 1033
CPXMI_KAPPA_UNSTABLE = 1034
CPXMI_LB_LARGE_NUM = 1003
CPXMI_LB_SMALL_NUM = 1004
CPXMI_LC_NZ_LARGE_NUM = 1023
CPXMI_LC_NZ_SMALL_NUM = 1024
CPXMI_LC_RHS_LARGE_NUM = 1025
CPXMI_LC_RHS_SMALL_NUM = 1026
CPXMI_MULTIOBJ_COEFFS = 1062
CPXMI_MULTIOBJ_LARGE_NUM = 1058
CPXMI_MULTIOBJ_MIX = 1063
CPXMI_MULTIOBJ_OPT_TOL = 1060
CPXMI_MULTIOBJ_SMALL_NUM = 1059
CPXMI_NZ_LARGE_NUM = 1009
CPXMI_NZ_SMALL_NUM = 1010
CPXMI_OBJ_LARGE_NUM = 1001
CPXMI_OBJ_SMALL_NUM = 1002
CPXMI_OPT_TOL = 1044
CPXMI_PWL_SLOPE_LARGE_NUM = 1064
CPXMI_PWL_SLOPE_SMALL_NUM = 1065
CPXMI_QC_LINNZ_LARGE_NUM = 1015
CPXMI_QC_LINNZ_SMALL_NUM = 1016
CPXMI_QC_QNZ_LARGE_NUM = 1017
CPXMI_QC_QNZ_SMALL_NUM = 1018
CPXMI_QC_RHS_LARGE_NUM = 1013
CPXMI_QC_RHS_SMALL_NUM = 1014
CPXMI_QOBJ_LARGE_NUM = 1011
CPXMI_QOBJ_SMALL_NUM = 1012
CPXMI_QOPT_TOL = 1046
CPXMI_RHS_LARGE_NUM = 1007
CPXMI_RHS_SMALL_NUM = 1008
CPXMI_SAMECOEFF_COL = 1050
CPXMI_SAMECOEFF_IND = 1051
CPXMI_SAMECOEFF_LAZY = 1054
CPXMI_SAMECOEFF_MULTIOBJ = 1061
CPXMI_SAMECOEFF_OBJ = 1057
CPXMI_SAMECOEFF_QLIN = 1052
CPXMI_SAMECOEFF_QUAD = 1053
CPXMI_SAMECOEFF_RHS = 1056
CPXMI_SAMECOEFF_ROW = 1049
CPXMI_SAMECOEFF_UCUT = 1055
CPXMI_SINGLE_PRECISION = 1036
CPXMI_SYMMETRY_BREAKING_INEQ = 1039
CPXMI_UB_LARGE_NUM = 1005
CPXMI_UB_SMALL_NUM = 1006
CPXMI_UC_NZ_LARGE_NUM = 1027
CPXMI_UC_NZ_SMALL_NUM = 1028
CPXMI_UC_RHS_LARGE_NUM = 1029
CPXMI_UC_RHS_SMALL_NUM = 1030
CPXMI_WIDE_COEFF_RANGE = 1048
CPXMIP_ABORT_FEAS = 113
CPXMIP_ABORT_INFEAS = 114
CPXMIP_ABORT_RELAXATION_UNBOUNDED = 133
CPXMIP_ABORT_RELAXED = 126
CPXMIP_DETTIME_LIM_FEAS = 131
CPXMIP_DETTIME_LIM_INFEAS = 132
CPXMIP_FAIL_FEAS = 109
CPXMIP_FAIL_FEAS_NO_TREE = 116
CPXMIP_FAIL_INFEAS = 110
CPXMIP_FAIL_INFEAS_NO_TREE = 117
CPXMIP_FEASIBLE = 127
CPXMIP_FEASIBLE_RELAXED_INF = 122
CPXMIP_FEASIBLE_RELAXED_QUAD = 124
CPXMIP_FEASIBLE_RELAXED_SUM = 120
CPXMIP_INFEASIBLE = 103
CPXMIP_INForUNBD = 119
CPXMIP_MEM_LIM_FEAS = 111
CPXMIP_MEM_LIM_INFEAS = 112
CPXMIP_NODE_LIM_FEAS = 105
CPXMIP_NODE_LIM_INFEAS = 106
CPXMIP_OPTIMAL = 101
CPXMIP_OPTIMAL_INFEAS = 115
CPXMIP_OPTIMAL_POPULATED = 129
CPXMIP_OPTIMAL_POPULATED_TOL = 130
CPXMIP_OPTIMAL_RELAXED_INF = 123
CPXMIP_OPTIMAL_RELAXED_QUAD = 125
CPXMIP_OPTIMAL_RELAXED_SUM = 121
CPXMIP_OPTIMAL_TOL = 102
CPXMIP_POPULATESOL_LIM = 128
CPXMIP_SOL_LIM = 104
CPXMIP_TIME_LIM_FEAS = 107
CPXMIP_TIME_LIM_INFEAS = 108
CPXMIP_UNBOUNDED = 118
CPX_PARAM_ADVIND = 1001
CPX_PARAM_AGGFILL = 1002
CPX_PARAM_AGGIND = 1003
CPX_PARAM_CLOCKTYPE = 1006
CPX_PARAM_CRAIND = 1007
CPX_PARAM_DEPIND = 1008
CPX_PARAM_DPRIIND = 1009
CPX_PARAM_PRICELIM = 1010
CPX_PARAM_EPMRK = 1013
CPX_PARAM_EPOPT = 1014
CPX_PARAM_EPPER = 1015
CPX_PARAM_EPRHS = 1016
CPX_PARAM_SIMDISPLAY = 1019
CPX_PARAM_ITLIM = 1020
CPX_PARAM_ROWREADLIM = 1021
CPX_PARAM_NETFIND = 1022
CPX_PARAM_COLREADLIM = 1023
CPX_PARAM_NZREADLIM = 1024
CPX_PARAM_OBJLLIM = 1025
CPX_PARAM_OBJULIM = 1026
CPX_PARAM_PERIND = 1027
CPX_PARAM_PERLIM = 1028
CPX_PARAM_PPRIIND = 1029
CPX_PARAM_PREIND = 1030
CPX_PARAM_REINV = 1031
CPX_PARAM_SCAIND = 1034
CPX_PARAM_SCRIND = 1035
CPX_PARAM_SINGLIM = 1037
CPX_PARAM_TILIM = 1039
CPX_PARAM_PREDUAL = 1044
CPX_PARAM_PREPASS = 1052
CPX_PARAM_DATACHECK = 1056
CPX_PARAM_REDUCE = 1057
CPX_PARAM_PRELINEAR = 1058
CPX_PARAM_LPMETHOD = 1062
CPX_PARAM_QPMETHOD = 1063
CPX_PARAM_WORKDIR = 1064
CPX_PARAM_WORKMEM = 1065
CPX_PARAM_THREADS = 1067
CPX_PARAM_CONFLICTALG = 1073
CPX_PARAM_CONFLICTDISPLAY = 1074
CPX_PARAM_SIFTDISPLAY = 1076
CPX_PARAM_SIFTALG = 1077
CPX_PARAM_SIFTITLIM = 1078
CPX_PARAM_MPSLONGNUM = 1081
CPX_PARAM_MEMORYEMPHASIS = 1082
CPX_PARAM_NUMERICALEMPHASIS = 1083
CPX_PARAM_FEASOPTMODE = 1084
CPX_PARAM_PARALLELMODE = 1109
CPX_PARAM_TUNINGMEASURE = 1110
CPX_PARAM_TUNINGREPEAT = 1111
CPX_PARAM_TUNINGTILIM = 1112
CPX_PARAM_TUNINGDISPLAY = 1113
CPX_PARAM_WRITELEVEL = 1114
CPX_PARAM_RANDOMSEED = 1124
CPX_PARAM_DETTILIM = 1127
CPX_PARAM_FILEENCODING = 1129
CPX_PARAM_APIENCODING = 1130
CPX_PARAM_OPTIMALITYTARGET = 1131
CPX_PARAM_CLONELOG = 1132
CPX_PARAM_TUNINGDETTILIM = 1139
CPX_PARAM_CPUMASK = 1144
CPX_PARAM_SOLUTIONTYPE = 1147
CPX_PARAM_WARNLIM = 1157
CPX_PARAM_SIFTSIM = 1158
CPX_PARAM_DYNAMICROWS = 1161
CPX_PARAM_RECORD = 1162
CPX_PARAM_PARAMDISPLAY = 1163
CPX_PARAM_FOLDING = 1164
CPX_PARAM_PREREFORM = 1167
CPX_PARAM_WORKERALG = 1500
CPX_PARAM_BENDERSSTRATEGY = 1501
CPX_PARAM_BENDERSFEASCUTTOL = 1509
CPX_PARAM_BENDERSOPTCUTTOL = 1510
CPX_PARAM_MULTIOBJDISPLAY = 1600
CPX_PARAM_BRDIR = 2001
CPX_PARAM_BTTOL = 2002
CPX_PARAM_CLIQUES = 2003
CPX_PARAM_COEREDIND = 2004
CPX_PARAM_COVERS = 2005
CPX_PARAM_CUTLO = 2006
CPX_PARAM_CUTUP = 2007
CPX_PARAM_EPAGAP = 2008
CPX_PARAM_EPGAP = 2009
CPX_PARAM_EPINT = 2010
CPX_PARAM_MIPDISPLAY = 2012
CPX_PARAM_MIPINTERVAL = 2013
CPX_PARAM_INTSOLLIM = 2015
CPX_PARAM_NODEFILEIND = 2016
CPX_PARAM_NODELIM = 2017
CPX_PARAM_NODESEL = 2018
CPX_PARAM_OBJDIF = 2019
CPX_PARAM_MIPORDIND = 2020
CPX_PARAM_RELOBJDIF = 2022
CPX_PARAM_STARTALG = 2025
CPX_PARAM_SUBALG = 2026
CPX_PARAM_TRELIM = 2027
CPX_PARAM_VARSEL = 2028
CPX_PARAM_BNDSTRENIND = 2029
CPX_PARAM_HEURFREQ = 2031
CPX_PARAM_MIPORDTYPE = 2032
CPX_PARAM_CUTSFACTOR = 2033
CPX_PARAM_RELAXPREIND = 2034
CPX_PARAM_PRESLVND = 2037
CPX_PARAM_BBINTERVAL = 2039
CPX_PARAM_FLOWCOVERS = 2040
CPX_PARAM_IMPLBD = 2041
CPX_PARAM_PROBE = 2042
CPX_PARAM_GUBCOVERS = 2044
CPX_PARAM_STRONGCANDLIM = 2045
CPX_PARAM_STRONGITLIM = 2046
CPX_PARAM_FRACCAND = 2048
CPX_PARAM_FRACCUTS = 2049
CPX_PARAM_FRACPASS = 2050
CPX_PARAM_FLOWPATHS = 2051
CPX_PARAM_MIRCUTS = 2052
CPX_PARAM_DISJCUTS = 2053
CPX_PARAM_AGGCUTLIM = 2054
CPX_PARAM_MIPCBREDLP = 2055
CPX_PARAM_CUTPASS = 2056
CPX_PARAM_MIPEMPHASIS = 2058
CPX_PARAM_SYMMETRY = 2059
CPX_PARAM_DIVETYPE = 2060
CPX_PARAM_RINSHEUR = 2061
CPX_PARAM_LBHEUR = 2063
CPX_PARAM_REPEATPRESOLVE = 2064
CPX_PARAM_PROBETIME = 2065
CPX_PARAM_REPAIRTRIES = 2067
CPX_PARAM_EPLIN = 2068
CPX_PARAM_EPRELAX = 2073
CPX_PARAM_FPHEUR = 2098
CPX_PARAM_EACHCUTLIM = 2102
CPX_PARAM_SOLNPOOLCAPACITY = 2103
CPX_PARAM_SOLNPOOLREPLACE = 2104
CPX_PARAM_SOLNPOOLGAP = 2105
CPX_PARAM_SOLNPOOLAGAP = 2106
CPX_PARAM_SOLNPOOLINTENSITY = 2107
CPX_PARAM_POPULATELIM = 2108
CPX_PARAM_MIPSEARCH = 2109
CPX_PARAM_MIQCPSTRAT = 2110
CPX_PARAM_ZEROHALFCUTS = 2111
CPX_PARAM_HEUREFFORT = 2120
CPX_PARAM_POLISHAFTEREPAGAP = 2126
CPX_PARAM_POLISHAFTEREPGAP = 2127
CPX_PARAM_POLISHAFTERNODE = 2128
CPX_PARAM_POLISHAFTERINTSOL = 2129
CPX_PARAM_POLISHAFTERTIME = 2130
CPX_PARAM_MCFCUTS = 2134
CPX_PARAM_MIPKAPPASTATS = 2137
CPX_PARAM_AUXROOTTHREADS = 2139
CPX_PARAM_INTSOLFILEPREFIX = 2143
CPX_PARAM_PROBEDETTIME = 2150
CPX_PARAM_POLISHAFTERDETTIME = 2151
CPX_PARAM_LANDPCUTS = 2152
CPX_PARAM_NODECUTS = 2157
CPX_PARAM_LOCALIMPLBD = 2181
CPX_PARAM_BQPCUTS = 2195
CPX_PARAM_RLTCUTS = 2196
CPX_PARAM_SUBMIPSTARTALG = 2205
CPX_PARAM_SUBMIPSUBALG = 2206
CPX_PARAM_SUBMIPSCAIND = 2207
CPX_PARAM_SUBMIPNODELIMIT = 2212
CPX_PARAM_SOS1REFORM = 2230
CPX_PARAM_SOS2REFORM = 2231
CPX_PARAM_LOWEROBJSTOP = 2233
CPX_PARAM_UPPEROBJSTOP = 2234
CPX_PARAM_CARDLS = 2235
CPX_PARAM_BAREPCOMP = 3002
CPX_PARAM_BARGROWTH = 3003
CPX_PARAM_BAROBJRNG = 3004
CPX_PARAM_BARALG = 3007
CPX_PARAM_BARCOLNZ = 3009
CPX_PARAM_BARDISPLAY = 3010
CPX_PARAM_BARITLIM = 3012
CPX_PARAM_BARMAXCOR = 3013
CPX_PARAM_BARORDER = 3014
CPX_PARAM_BARSTARTALG = 3017
CPX_PARAM_BARCROSSALG = 3018
CPX_PARAM_BARQCPEPCOMP = 3020
CPX_PARAM_QPNZREADLIM = 4001
CPX_PARAM_CALCQCPDUALS = 4003
CPX_PARAM_QPMAKEPSDIND = 4010
CPX_PARAM_QTOLININD = 4012
CPX_PARAM_NETITLIM = 5001
CPX_PARAM_NETEPOPT = 5002
CPX_PARAM_NETEPRHS = 5003
CPX_PARAM_NETPPRIIND = 5004
CPX_PARAM_NETDISPLAY = 5005
