// Generated from c:/Users/solar/OneDrive/Documents/Capstone/Capstone-project/source_files/Esgish2Grammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class Esgish2GrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, SAVED_SCREEN=4, FACTOR=5, CUSTOM_SCORE=6, OP_NULL_TYPE=7, 
		OP_BOOLEAN=8, OP_ORDER=9, OP_STRING_MATCH=10, OP_STRING_LIST=11, OP_STRING_MAP=12, 
		OP_STRING_LIST_NO_ARG=13, OP_DATE=14, CASE_COUNT=15, IF=16, PERSON_COUNT=17, 
		PERCENTILE_RANK_IN_CATEGORY=18, PERCENTILE_RANK=19, QUANTILE=20, QUANTILE_IN_CATEGORY=21, 
		RANK_ASCENDING=22, RANK_DESCENDING=23, SUM=24, DIFFERENCE=25, COALESCE=26, 
		RATIO=27, YEARS_SINCE=28, BOOLEAN=29, AND=30, OR=31, NOT=32, BO=33, BC=34, 
		NULL=35, NULL_LIST=36, ARG=37, WS=38;
	public static final int
		RULE_start = 0, RULE_query = 1, RULE_wrappedQuery = 2, RULE_singleFactorQuery = 3, 
		RULE_booleanQuery = 4, RULE_dateQuery = 5, RULE_formulaQuery = 6, RULE_nullTypeQuery = 7, 
		RULE_numberOrStringQuery = 8, RULE_stringListQuery = 9, RULE_stringMapQuery = 10, 
		RULE_stringQuery = 11, RULE_savedQuery = 12, RULE_wrappedSavedQuery = 13, 
		RULE_customScoreQuery = 14, RULE_andQuery = 15, RULE_orQuery = 16, RULE_negatedQuery = 17, 
		RULE_groupQueryElement = 18, RULE_formula = 19, RULE_ratioFormula = 20, 
		RULE_coalesceFormula = 21, RULE_caseCountFormula = 22, RULE_ifFormula = 23, 
		RULE_personCountFormula = 24, RULE_percentileRankFormula = 25, RULE_percentileRankInCategoryFormula = 26, 
		RULE_quantileFormula = 27, RULE_quantileFormulaInCategoryFormula = 28, 
		RULE_rankAscendingFormula = 29, RULE_rankDescendingFormula = 30, RULE_sumFormula = 31, 
		RULE_differenceFormula = 32, RULE_yearsSinceFormula = 33, RULE_booleanFormula = 34;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "query", "wrappedQuery", "singleFactorQuery", "booleanQuery", 
			"dateQuery", "formulaQuery", "nullTypeQuery", "numberOrStringQuery", 
			"stringListQuery", "stringMapQuery", "stringQuery", "savedQuery", "wrappedSavedQuery", 
			"customScoreQuery", "andQuery", "orQuery", "negatedQuery", "groupQueryElement", 
			"formula", "ratioFormula", "coalesceFormula", "caseCountFormula", "ifFormula", 
			"personCountFormula", "percentileRankFormula", "percentileRankInCategoryFormula", 
			"quantileFormula", "quantileFormulaInCategoryFormula", "rankAscendingFormula", 
			"rankDescendingFormula", "sumFormula", "differenceFormula", "yearsSinceFormula", 
			"booleanFormula"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "','", null, null, null, "'IS'", null, null, null, 
			null, null, "'EMPTY'", null, "'CASE_COUNT'", "'IF'", "'PERSON_COUNT'", 
			"'PERCENTILE_RANK_IN_CATEGORY'", "'PERCENTILE_RANK'", "'QUANTILE'", "'QUANTILE_IN_CATEGORY'", 
			"'RANK_ASCENDING'", "'RANK_DESCENDING'", "'SUM'", "'DIFFERENCE'", "'COALESCE'", 
			"'RATIO'", "'YEARS_SINCE'", "'BOOLEAN'", "'AND'", "'OR'", "'NOT'", "'['", 
			"']'", "'NULL'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "SAVED_SCREEN", "FACTOR", "CUSTOM_SCORE", "OP_NULL_TYPE", 
			"OP_BOOLEAN", "OP_ORDER", "OP_STRING_MATCH", "OP_STRING_LIST", "OP_STRING_MAP", 
			"OP_STRING_LIST_NO_ARG", "OP_DATE", "CASE_COUNT", "IF", "PERSON_COUNT", 
			"PERCENTILE_RANK_IN_CATEGORY", "PERCENTILE_RANK", "QUANTILE", "QUANTILE_IN_CATEGORY", 
			"RANK_ASCENDING", "RANK_DESCENDING", "SUM", "DIFFERENCE", "COALESCE", 
			"RATIO", "YEARS_SINCE", "BOOLEAN", "AND", "OR", "NOT", "BO", "BC", "NULL", 
			"NULL_LIST", "ARG", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Esgish2Grammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public Esgish2GrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StartContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(Esgish2GrammarParser.EOF, 0); }
		public QueryContext query() {
			return getRuleContext(QueryContext.class,0);
		}
		public WrappedQueryContext wrappedQuery() {
			return getRuleContext(WrappedQueryContext.class,0);
		}
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(70);
				query();
				}
				break;
			case 2:
				{
				setState(71);
				wrappedQuery();
				}
				break;
			case 3:
				{
				setState(72);
				formula();
				}
				break;
			}
			setState(75);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryContext extends ParserRuleContext {
		public SingleFactorQueryContext singleFactorQuery() {
			return getRuleContext(SingleFactorQueryContext.class,0);
		}
		public AndQueryContext andQuery() {
			return getRuleContext(AndQueryContext.class,0);
		}
		public OrQueryContext orQuery() {
			return getRuleContext(OrQueryContext.class,0);
		}
		public NegatedQueryContext negatedQuery() {
			return getRuleContext(NegatedQueryContext.class,0);
		}
		public SavedQueryContext savedQuery() {
			return getRuleContext(SavedQueryContext.class,0);
		}
		public CustomScoreQueryContext customScoreQuery() {
			return getRuleContext(CustomScoreQueryContext.class,0);
		}
		public QueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query; }
	}

	public final QueryContext query() throws RecognitionException {
		QueryContext _localctx = new QueryContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_query);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(77);
				singleFactorQuery();
				}
				break;
			case 2:
				{
				setState(78);
				andQuery();
				}
				break;
			case 3:
				{
				setState(79);
				orQuery();
				}
				break;
			case 4:
				{
				setState(80);
				negatedQuery();
				}
				break;
			case 5:
				{
				setState(81);
				savedQuery();
				}
				break;
			case 6:
				{
				setState(82);
				customScoreQuery();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WrappedQueryContext extends ParserRuleContext {
		public QueryContext query() {
			return getRuleContext(QueryContext.class,0);
		}
		public WrappedQueryContext wrappedQuery() {
			return getRuleContext(WrappedQueryContext.class,0);
		}
		public WrappedQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wrappedQuery; }
	}

	public final WrappedQueryContext wrappedQuery() throws RecognitionException {
		WrappedQueryContext _localctx = new WrappedQueryContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_wrappedQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(T__0);
			setState(88);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SAVED_SCREEN:
			case FACTOR:
			case CUSTOM_SCORE:
			case CASE_COUNT:
			case IF:
			case PERSON_COUNT:
			case PERCENTILE_RANK_IN_CATEGORY:
			case PERCENTILE_RANK:
			case QUANTILE:
			case QUANTILE_IN_CATEGORY:
			case RANK_ASCENDING:
			case RANK_DESCENDING:
			case SUM:
			case DIFFERENCE:
			case COALESCE:
			case RATIO:
			case YEARS_SINCE:
			case BOOLEAN:
			case AND:
			case OR:
			case NOT:
				{
				setState(86);
				query();
				}
				break;
			case T__0:
				{
				setState(87);
				wrappedQuery();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(90);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SingleFactorQueryContext extends ParserRuleContext {
		public BooleanQueryContext booleanQuery() {
			return getRuleContext(BooleanQueryContext.class,0);
		}
		public CustomScoreQueryContext customScoreQuery() {
			return getRuleContext(CustomScoreQueryContext.class,0);
		}
		public DateQueryContext dateQuery() {
			return getRuleContext(DateQueryContext.class,0);
		}
		public FormulaQueryContext formulaQuery() {
			return getRuleContext(FormulaQueryContext.class,0);
		}
		public NullTypeQueryContext nullTypeQuery() {
			return getRuleContext(NullTypeQueryContext.class,0);
		}
		public NumberOrStringQueryContext numberOrStringQuery() {
			return getRuleContext(NumberOrStringQueryContext.class,0);
		}
		public StringListQueryContext stringListQuery() {
			return getRuleContext(StringListQueryContext.class,0);
		}
		public StringMapQueryContext stringMapQuery() {
			return getRuleContext(StringMapQueryContext.class,0);
		}
		public StringQueryContext stringQuery() {
			return getRuleContext(StringQueryContext.class,0);
		}
		public NegatedQueryContext negatedQuery() {
			return getRuleContext(NegatedQueryContext.class,0);
		}
		public SingleFactorQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleFactorQuery; }
	}

	public final SingleFactorQueryContext singleFactorQuery() throws RecognitionException {
		SingleFactorQueryContext _localctx = new SingleFactorQueryContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_singleFactorQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(92);
				booleanQuery();
				}
				break;
			case 2:
				{
				setState(93);
				customScoreQuery();
				}
				break;
			case 3:
				{
				setState(94);
				dateQuery();
				}
				break;
			case 4:
				{
				setState(95);
				formulaQuery();
				}
				break;
			case 5:
				{
				setState(96);
				nullTypeQuery();
				}
				break;
			case 6:
				{
				setState(97);
				numberOrStringQuery();
				}
				break;
			case 7:
				{
				setState(98);
				stringListQuery();
				}
				break;
			case 8:
				{
				setState(99);
				stringMapQuery();
				}
				break;
			case 9:
				{
				setState(100);
				stringQuery();
				}
				break;
			case 10:
				{
				setState(101);
				negatedQuery();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BooleanQueryContext extends ParserRuleContext {
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public TerminalNode OP_BOOLEAN() { return getToken(Esgish2GrammarParser.OP_BOOLEAN, 0); }
		public TerminalNode NULL_LIST() { return getToken(Esgish2GrammarParser.NULL_LIST, 0); }
		public BooleanQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_booleanQuery; }
	}

	public final BooleanQueryContext booleanQuery() throws RecognitionException {
		BooleanQueryContext _localctx = new BooleanQueryContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_booleanQuery);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(FACTOR);
			setState(105);
			match(OP_BOOLEAN);
			setState(107);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NULL_LIST) {
				{
				setState(106);
				match(NULL_LIST);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DateQueryContext extends ParserRuleContext {
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public TerminalNode OP_DATE() { return getToken(Esgish2GrammarParser.OP_DATE, 0); }
		public TerminalNode ARG() { return getToken(Esgish2GrammarParser.ARG, 0); }
		public TerminalNode NULL_LIST() { return getToken(Esgish2GrammarParser.NULL_LIST, 0); }
		public DateQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dateQuery; }
	}

	public final DateQueryContext dateQuery() throws RecognitionException {
		DateQueryContext _localctx = new DateQueryContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_dateQuery);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(FACTOR);
			setState(110);
			match(OP_DATE);
			setState(111);
			match(ARG);
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NULL_LIST) {
				{
				setState(112);
				match(NULL_LIST);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FormulaQueryContext extends ParserRuleContext {
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public TerminalNode OP_ORDER() { return getToken(Esgish2GrammarParser.OP_ORDER, 0); }
		public TerminalNode ARG() { return getToken(Esgish2GrammarParser.ARG, 0); }
		public TerminalNode NULL_LIST() { return getToken(Esgish2GrammarParser.NULL_LIST, 0); }
		public FormulaQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formulaQuery; }
	}

	public final FormulaQueryContext formulaQuery() throws RecognitionException {
		FormulaQueryContext _localctx = new FormulaQueryContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_formulaQuery);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			formula();
			setState(116);
			match(OP_ORDER);
			setState(117);
			match(ARG);
			setState(119);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NULL_LIST) {
				{
				setState(118);
				match(NULL_LIST);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NullTypeQueryContext extends ParserRuleContext {
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public TerminalNode OP_NULL_TYPE() { return getToken(Esgish2GrammarParser.OP_NULL_TYPE, 0); }
		public TerminalNode NULL() { return getToken(Esgish2GrammarParser.NULL, 0); }
		public TerminalNode NULL_LIST() { return getToken(Esgish2GrammarParser.NULL_LIST, 0); }
		public NullTypeQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nullTypeQuery; }
	}

	public final NullTypeQueryContext nullTypeQuery() throws RecognitionException {
		NullTypeQueryContext _localctx = new NullTypeQueryContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_nullTypeQuery);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			match(FACTOR);
			setState(122);
			match(OP_NULL_TYPE);
			setState(127);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EOF:
			case T__1:
			case T__2:
			case NULL_LIST:
				{
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NULL_LIST) {
					{
					setState(123);
					match(NULL_LIST);
					}
				}

				}
				break;
			case NULL:
				{
				setState(126);
				match(NULL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumberOrStringQueryContext extends ParserRuleContext {
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public TerminalNode OP_ORDER() { return getToken(Esgish2GrammarParser.OP_ORDER, 0); }
		public TerminalNode ARG() { return getToken(Esgish2GrammarParser.ARG, 0); }
		public TerminalNode NULL_LIST() { return getToken(Esgish2GrammarParser.NULL_LIST, 0); }
		public NumberOrStringQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numberOrStringQuery; }
	}

	public final NumberOrStringQueryContext numberOrStringQuery() throws RecognitionException {
		NumberOrStringQueryContext _localctx = new NumberOrStringQueryContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_numberOrStringQuery);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(FACTOR);
			setState(130);
			match(OP_ORDER);
			setState(131);
			match(ARG);
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NULL_LIST) {
				{
				setState(132);
				match(NULL_LIST);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringListQueryContext extends ParserRuleContext {
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public TerminalNode OP_STRING_LIST() { return getToken(Esgish2GrammarParser.OP_STRING_LIST, 0); }
		public TerminalNode ARG() { return getToken(Esgish2GrammarParser.ARG, 0); }
		public TerminalNode OP_STRING_LIST_NO_ARG() { return getToken(Esgish2GrammarParser.OP_STRING_LIST_NO_ARG, 0); }
		public TerminalNode NULL_LIST() { return getToken(Esgish2GrammarParser.NULL_LIST, 0); }
		public StringListQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringListQuery; }
	}

	public final StringListQueryContext stringListQuery() throws RecognitionException {
		StringListQueryContext _localctx = new StringListQueryContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_stringListQuery);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(135);
				match(FACTOR);
				setState(136);
				match(OP_STRING_LIST);
				setState(137);
				match(ARG);
				}
				break;
			case 2:
				{
				setState(138);
				match(FACTOR);
				setState(139);
				match(OP_STRING_LIST_NO_ARG);
				}
				break;
			}
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NULL_LIST) {
				{
				setState(142);
				match(NULL_LIST);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringMapQueryContext extends ParserRuleContext {
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public TerminalNode OP_STRING_MAP() { return getToken(Esgish2GrammarParser.OP_STRING_MAP, 0); }
		public TerminalNode ARG() { return getToken(Esgish2GrammarParser.ARG, 0); }
		public TerminalNode NULL_LIST() { return getToken(Esgish2GrammarParser.NULL_LIST, 0); }
		public StringMapQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringMapQuery; }
	}

	public final StringMapQueryContext stringMapQuery() throws RecognitionException {
		StringMapQueryContext _localctx = new StringMapQueryContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_stringMapQuery);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			match(FACTOR);
			setState(146);
			match(OP_STRING_MAP);
			setState(147);
			match(ARG);
			setState(149);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NULL_LIST) {
				{
				setState(148);
				match(NULL_LIST);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringQueryContext extends ParserRuleContext {
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public TerminalNode OP_STRING_MATCH() { return getToken(Esgish2GrammarParser.OP_STRING_MATCH, 0); }
		public TerminalNode ARG() { return getToken(Esgish2GrammarParser.ARG, 0); }
		public TerminalNode NULL_LIST() { return getToken(Esgish2GrammarParser.NULL_LIST, 0); }
		public StringQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringQuery; }
	}

	public final StringQueryContext stringQuery() throws RecognitionException {
		StringQueryContext _localctx = new StringQueryContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_stringQuery);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			match(FACTOR);
			setState(152);
			match(OP_STRING_MATCH);
			setState(153);
			match(ARG);
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NULL_LIST) {
				{
				setState(154);
				match(NULL_LIST);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SavedQueryContext extends ParserRuleContext {
		public TerminalNode SAVED_SCREEN() { return getToken(Esgish2GrammarParser.SAVED_SCREEN, 0); }
		public TerminalNode OP_BOOLEAN() { return getToken(Esgish2GrammarParser.OP_BOOLEAN, 0); }
		public SavedQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_savedQuery; }
	}

	public final SavedQueryContext savedQuery() throws RecognitionException {
		SavedQueryContext _localctx = new SavedQueryContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_savedQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(SAVED_SCREEN);
			setState(158);
			match(OP_BOOLEAN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WrappedSavedQueryContext extends ParserRuleContext {
		public SavedQueryContext savedQuery() {
			return getRuleContext(SavedQueryContext.class,0);
		}
		public WrappedSavedQueryContext wrappedSavedQuery() {
			return getRuleContext(WrappedSavedQueryContext.class,0);
		}
		public WrappedSavedQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wrappedSavedQuery; }
	}

	public final WrappedSavedQueryContext wrappedSavedQuery() throws RecognitionException {
		WrappedSavedQueryContext _localctx = new WrappedSavedQueryContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_wrappedSavedQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(T__0);
			setState(163);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SAVED_SCREEN:
				{
				setState(161);
				savedQuery();
				}
				break;
			case T__0:
				{
				setState(162);
				wrappedSavedQuery();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(165);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CustomScoreQueryContext extends ParserRuleContext {
		public TerminalNode CUSTOM_SCORE() { return getToken(Esgish2GrammarParser.CUSTOM_SCORE, 0); }
		public TerminalNode OP_ORDER() { return getToken(Esgish2GrammarParser.OP_ORDER, 0); }
		public TerminalNode ARG() { return getToken(Esgish2GrammarParser.ARG, 0); }
		public CustomScoreQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_customScoreQuery; }
	}

	public final CustomScoreQueryContext customScoreQuery() throws RecognitionException {
		CustomScoreQueryContext _localctx = new CustomScoreQueryContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_customScoreQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(CUSTOM_SCORE);
			setState(168);
			match(OP_ORDER);
			setState(169);
			match(ARG);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AndQueryContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(Esgish2GrammarParser.AND, 0); }
		public List<GroupQueryElementContext> groupQueryElement() {
			return getRuleContexts(GroupQueryElementContext.class);
		}
		public GroupQueryElementContext groupQueryElement(int i) {
			return getRuleContext(GroupQueryElementContext.class,i);
		}
		public AndQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andQuery; }
	}

	public final AndQueryContext andQuery() throws RecognitionException {
		AndQueryContext _localctx = new AndQueryContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_andQuery);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			match(AND);
			setState(172);
			match(T__0);
			setState(173);
			groupQueryElement();
			setState(176); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(174);
				match(T__2);
				setState(175);
				groupQueryElement();
				}
				}
				setState(178); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__2 );
			setState(180);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OrQueryContext extends ParserRuleContext {
		public TerminalNode OR() { return getToken(Esgish2GrammarParser.OR, 0); }
		public List<GroupQueryElementContext> groupQueryElement() {
			return getRuleContexts(GroupQueryElementContext.class);
		}
		public GroupQueryElementContext groupQueryElement(int i) {
			return getRuleContext(GroupQueryElementContext.class,i);
		}
		public OrQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orQuery; }
	}

	public final OrQueryContext orQuery() throws RecognitionException {
		OrQueryContext _localctx = new OrQueryContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_orQuery);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(OR);
			setState(183);
			match(T__0);
			setState(184);
			groupQueryElement();
			setState(187); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(185);
				match(T__2);
				setState(186);
				groupQueryElement();
				}
				}
				setState(189); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__2 );
			setState(191);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NegatedQueryContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(Esgish2GrammarParser.NOT, 0); }
		public WrappedQueryContext wrappedQuery() {
			return getRuleContext(WrappedQueryContext.class,0);
		}
		public NegatedQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_negatedQuery; }
	}

	public final NegatedQueryContext negatedQuery() throws RecognitionException {
		NegatedQueryContext _localctx = new NegatedQueryContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_negatedQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			match(NOT);
			setState(194);
			wrappedQuery();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GroupQueryElementContext extends ParserRuleContext {
		public SingleFactorQueryContext singleFactorQuery() {
			return getRuleContext(SingleFactorQueryContext.class,0);
		}
		public AndQueryContext andQuery() {
			return getRuleContext(AndQueryContext.class,0);
		}
		public NegatedQueryContext negatedQuery() {
			return getRuleContext(NegatedQueryContext.class,0);
		}
		public OrQueryContext orQuery() {
			return getRuleContext(OrQueryContext.class,0);
		}
		public SavedQueryContext savedQuery() {
			return getRuleContext(SavedQueryContext.class,0);
		}
		public FormulaContext formula() {
			return getRuleContext(FormulaContext.class,0);
		}
		public GroupQueryElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_groupQueryElement; }
	}

	public final GroupQueryElementContext groupQueryElement() throws RecognitionException {
		GroupQueryElementContext _localctx = new GroupQueryElementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_groupQueryElement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(196);
				singleFactorQuery();
				}
				break;
			case 2:
				{
				setState(197);
				andQuery();
				}
				break;
			case 3:
				{
				setState(198);
				negatedQuery();
				}
				break;
			case 4:
				{
				setState(199);
				orQuery();
				}
				break;
			case 5:
				{
				setState(200);
				savedQuery();
				}
				break;
			case 6:
				{
				setState(201);
				formula();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FormulaContext extends ParserRuleContext {
		public CaseCountFormulaContext caseCountFormula() {
			return getRuleContext(CaseCountFormulaContext.class,0);
		}
		public IfFormulaContext ifFormula() {
			return getRuleContext(IfFormulaContext.class,0);
		}
		public PersonCountFormulaContext personCountFormula() {
			return getRuleContext(PersonCountFormulaContext.class,0);
		}
		public PercentileRankFormulaContext percentileRankFormula() {
			return getRuleContext(PercentileRankFormulaContext.class,0);
		}
		public PercentileRankInCategoryFormulaContext percentileRankInCategoryFormula() {
			return getRuleContext(PercentileRankInCategoryFormulaContext.class,0);
		}
		public QuantileFormulaContext quantileFormula() {
			return getRuleContext(QuantileFormulaContext.class,0);
		}
		public QuantileFormulaInCategoryFormulaContext quantileFormulaInCategoryFormula() {
			return getRuleContext(QuantileFormulaInCategoryFormulaContext.class,0);
		}
		public RankAscendingFormulaContext rankAscendingFormula() {
			return getRuleContext(RankAscendingFormulaContext.class,0);
		}
		public RankDescendingFormulaContext rankDescendingFormula() {
			return getRuleContext(RankDescendingFormulaContext.class,0);
		}
		public SumFormulaContext sumFormula() {
			return getRuleContext(SumFormulaContext.class,0);
		}
		public DifferenceFormulaContext differenceFormula() {
			return getRuleContext(DifferenceFormulaContext.class,0);
		}
		public CoalesceFormulaContext coalesceFormula() {
			return getRuleContext(CoalesceFormulaContext.class,0);
		}
		public RatioFormulaContext ratioFormula() {
			return getRuleContext(RatioFormulaContext.class,0);
		}
		public YearsSinceFormulaContext yearsSinceFormula() {
			return getRuleContext(YearsSinceFormulaContext.class,0);
		}
		public BooleanFormulaContext booleanFormula() {
			return getRuleContext(BooleanFormulaContext.class,0);
		}
		public FormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formula; }
	}

	public final FormulaContext formula() throws RecognitionException {
		FormulaContext _localctx = new FormulaContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_formula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CASE_COUNT:
				{
				setState(204);
				caseCountFormula();
				}
				break;
			case IF:
				{
				setState(205);
				ifFormula();
				}
				break;
			case PERSON_COUNT:
				{
				setState(206);
				personCountFormula();
				}
				break;
			case PERCENTILE_RANK:
				{
				setState(207);
				percentileRankFormula();
				}
				break;
			case PERCENTILE_RANK_IN_CATEGORY:
				{
				setState(208);
				percentileRankInCategoryFormula();
				}
				break;
			case QUANTILE:
				{
				setState(209);
				quantileFormula();
				}
				break;
			case QUANTILE_IN_CATEGORY:
				{
				setState(210);
				quantileFormulaInCategoryFormula();
				}
				break;
			case RANK_ASCENDING:
				{
				setState(211);
				rankAscendingFormula();
				}
				break;
			case RANK_DESCENDING:
				{
				setState(212);
				rankDescendingFormula();
				}
				break;
			case SUM:
				{
				setState(213);
				sumFormula();
				}
				break;
			case DIFFERENCE:
				{
				setState(214);
				differenceFormula();
				}
				break;
			case COALESCE:
				{
				setState(215);
				coalesceFormula();
				}
				break;
			case RATIO:
				{
				setState(216);
				ratioFormula();
				}
				break;
			case YEARS_SINCE:
				{
				setState(217);
				yearsSinceFormula();
				}
				break;
			case BOOLEAN:
				{
				setState(218);
				booleanFormula();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RatioFormulaContext extends ParserRuleContext {
		public TerminalNode RATIO() { return getToken(Esgish2GrammarParser.RATIO, 0); }
		public List<TerminalNode> FACTOR() { return getTokens(Esgish2GrammarParser.FACTOR); }
		public TerminalNode FACTOR(int i) {
			return getToken(Esgish2GrammarParser.FACTOR, i);
		}
		public RatioFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ratioFormula; }
	}

	public final RatioFormulaContext ratioFormula() throws RecognitionException {
		RatioFormulaContext _localctx = new RatioFormulaContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_ratioFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			match(RATIO);
			setState(222);
			match(T__0);
			setState(223);
			match(FACTOR);
			setState(224);
			match(T__2);
			setState(225);
			match(FACTOR);
			setState(226);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CoalesceFormulaContext extends ParserRuleContext {
		public TerminalNode COALESCE() { return getToken(Esgish2GrammarParser.COALESCE, 0); }
		public List<TerminalNode> FACTOR() { return getTokens(Esgish2GrammarParser.FACTOR); }
		public TerminalNode FACTOR(int i) {
			return getToken(Esgish2GrammarParser.FACTOR, i);
		}
		public CoalesceFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_coalesceFormula; }
	}

	public final CoalesceFormulaContext coalesceFormula() throws RecognitionException {
		CoalesceFormulaContext _localctx = new CoalesceFormulaContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_coalesceFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(COALESCE);
			setState(229);
			match(T__0);
			setState(230);
			match(FACTOR);
			setState(231);
			match(T__2);
			setState(232);
			match(FACTOR);
			setState(233);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CaseCountFormulaContext extends ParserRuleContext {
		public TerminalNode CASE_COUNT() { return getToken(Esgish2GrammarParser.CASE_COUNT, 0); }
		public QueryContext query() {
			return getRuleContext(QueryContext.class,0);
		}
		public CaseCountFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_caseCountFormula; }
	}

	public final CaseCountFormulaContext caseCountFormula() throws RecognitionException {
		CaseCountFormulaContext _localctx = new CaseCountFormulaContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_caseCountFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			match(CASE_COUNT);
			setState(236);
			match(T__0);
			setState(237);
			query();
			setState(238);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfFormulaContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(Esgish2GrammarParser.IF, 0); }
		public List<TerminalNode> ARG() { return getTokens(Esgish2GrammarParser.ARG); }
		public TerminalNode ARG(int i) {
			return getToken(Esgish2GrammarParser.ARG, i);
		}
		public List<TerminalNode> NULL_LIST() { return getTokens(Esgish2GrammarParser.NULL_LIST); }
		public TerminalNode NULL_LIST(int i) {
			return getToken(Esgish2GrammarParser.NULL_LIST, i);
		}
		public List<SingleFactorQueryContext> singleFactorQuery() {
			return getRuleContexts(SingleFactorQueryContext.class);
		}
		public SingleFactorQueryContext singleFactorQuery(int i) {
			return getRuleContext(SingleFactorQueryContext.class,i);
		}
		public IfFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifFormula; }
	}

	public final IfFormulaContext ifFormula() throws RecognitionException {
		IfFormulaContext _localctx = new IfFormulaContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_ifFormula);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(240);
			match(IF);
			setState(241);
			match(T__0);
			setState(247); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(242);
				singleFactorQuery();
				setState(243);
				match(T__2);
				setState(244);
				_la = _input.LA(1);
				if ( !(_la==NULL_LIST || _la==ARG) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(245);
				match(T__2);
				}
				}
				setState(249); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 5368676448L) != 0) );
			setState(251);
			_la = _input.LA(1);
			if ( !(_la==NULL_LIST || _la==ARG) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(252);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PersonCountFormulaContext extends ParserRuleContext {
		public TerminalNode PERSON_COUNT() { return getToken(Esgish2GrammarParser.PERSON_COUNT, 0); }
		public QueryContext query() {
			return getRuleContext(QueryContext.class,0);
		}
		public PersonCountFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_personCountFormula; }
	}

	public final PersonCountFormulaContext personCountFormula() throws RecognitionException {
		PersonCountFormulaContext _localctx = new PersonCountFormulaContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_personCountFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			match(PERSON_COUNT);
			setState(255);
			match(T__0);
			setState(256);
			query();
			setState(257);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PercentileRankFormulaContext extends ParserRuleContext {
		public TerminalNode PERCENTILE_RANK() { return getToken(Esgish2GrammarParser.PERCENTILE_RANK, 0); }
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public PercentileRankFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_percentileRankFormula; }
	}

	public final PercentileRankFormulaContext percentileRankFormula() throws RecognitionException {
		PercentileRankFormulaContext _localctx = new PercentileRankFormulaContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_percentileRankFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(259);
			match(PERCENTILE_RANK);
			setState(260);
			match(T__0);
			setState(261);
			match(FACTOR);
			setState(262);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PercentileRankInCategoryFormulaContext extends ParserRuleContext {
		public TerminalNode PERCENTILE_RANK_IN_CATEGORY() { return getToken(Esgish2GrammarParser.PERCENTILE_RANK_IN_CATEGORY, 0); }
		public List<TerminalNode> FACTOR() { return getTokens(Esgish2GrammarParser.FACTOR); }
		public TerminalNode FACTOR(int i) {
			return getToken(Esgish2GrammarParser.FACTOR, i);
		}
		public PercentileRankInCategoryFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_percentileRankInCategoryFormula; }
	}

	public final PercentileRankInCategoryFormulaContext percentileRankInCategoryFormula() throws RecognitionException {
		PercentileRankInCategoryFormulaContext _localctx = new PercentileRankInCategoryFormulaContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_percentileRankInCategoryFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			match(PERCENTILE_RANK_IN_CATEGORY);
			setState(265);
			match(T__0);
			setState(266);
			match(FACTOR);
			setState(267);
			match(T__2);
			setState(268);
			match(FACTOR);
			setState(269);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QuantileFormulaContext extends ParserRuleContext {
		public TerminalNode QUANTILE() { return getToken(Esgish2GrammarParser.QUANTILE, 0); }
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public TerminalNode ARG() { return getToken(Esgish2GrammarParser.ARG, 0); }
		public QuantileFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_quantileFormula; }
	}

	public final QuantileFormulaContext quantileFormula() throws RecognitionException {
		QuantileFormulaContext _localctx = new QuantileFormulaContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_quantileFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			match(QUANTILE);
			setState(272);
			match(T__0);
			setState(273);
			match(FACTOR);
			setState(274);
			match(T__2);
			setState(275);
			match(ARG);
			setState(276);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QuantileFormulaInCategoryFormulaContext extends ParserRuleContext {
		public TerminalNode QUANTILE_IN_CATEGORY() { return getToken(Esgish2GrammarParser.QUANTILE_IN_CATEGORY, 0); }
		public List<TerminalNode> FACTOR() { return getTokens(Esgish2GrammarParser.FACTOR); }
		public TerminalNode FACTOR(int i) {
			return getToken(Esgish2GrammarParser.FACTOR, i);
		}
		public TerminalNode ARG() { return getToken(Esgish2GrammarParser.ARG, 0); }
		public QuantileFormulaInCategoryFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_quantileFormulaInCategoryFormula; }
	}

	public final QuantileFormulaInCategoryFormulaContext quantileFormulaInCategoryFormula() throws RecognitionException {
		QuantileFormulaInCategoryFormulaContext _localctx = new QuantileFormulaInCategoryFormulaContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_quantileFormulaInCategoryFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(278);
			match(QUANTILE_IN_CATEGORY);
			setState(279);
			match(T__0);
			setState(280);
			match(FACTOR);
			setState(281);
			match(T__2);
			setState(282);
			match(FACTOR);
			setState(283);
			match(T__2);
			setState(284);
			match(ARG);
			setState(285);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RankAscendingFormulaContext extends ParserRuleContext {
		public TerminalNode RANK_ASCENDING() { return getToken(Esgish2GrammarParser.RANK_ASCENDING, 0); }
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public RankAscendingFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rankAscendingFormula; }
	}

	public final RankAscendingFormulaContext rankAscendingFormula() throws RecognitionException {
		RankAscendingFormulaContext _localctx = new RankAscendingFormulaContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_rankAscendingFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(287);
			match(RANK_ASCENDING);
			setState(288);
			match(T__0);
			setState(289);
			match(FACTOR);
			setState(290);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RankDescendingFormulaContext extends ParserRuleContext {
		public TerminalNode RANK_DESCENDING() { return getToken(Esgish2GrammarParser.RANK_DESCENDING, 0); }
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public RankDescendingFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rankDescendingFormula; }
	}

	public final RankDescendingFormulaContext rankDescendingFormula() throws RecognitionException {
		RankDescendingFormulaContext _localctx = new RankDescendingFormulaContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_rankDescendingFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			match(RANK_DESCENDING);
			setState(293);
			match(T__0);
			setState(294);
			match(FACTOR);
			setState(295);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SumFormulaContext extends ParserRuleContext {
		public TerminalNode SUM() { return getToken(Esgish2GrammarParser.SUM, 0); }
		public List<TerminalNode> FACTOR() { return getTokens(Esgish2GrammarParser.FACTOR); }
		public TerminalNode FACTOR(int i) {
			return getToken(Esgish2GrammarParser.FACTOR, i);
		}
		public SumFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sumFormula; }
	}

	public final SumFormulaContext sumFormula() throws RecognitionException {
		SumFormulaContext _localctx = new SumFormulaContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_sumFormula);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			match(SUM);
			setState(298);
			match(T__0);
			setState(299);
			match(FACTOR);
			setState(302); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(300);
				match(T__2);
				setState(301);
				match(FACTOR);
				}
				}
				setState(304); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__2 );
			setState(306);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DifferenceFormulaContext extends ParserRuleContext {
		public TerminalNode DIFFERENCE() { return getToken(Esgish2GrammarParser.DIFFERENCE, 0); }
		public List<TerminalNode> FACTOR() { return getTokens(Esgish2GrammarParser.FACTOR); }
		public TerminalNode FACTOR(int i) {
			return getToken(Esgish2GrammarParser.FACTOR, i);
		}
		public DifferenceFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_differenceFormula; }
	}

	public final DifferenceFormulaContext differenceFormula() throws RecognitionException {
		DifferenceFormulaContext _localctx = new DifferenceFormulaContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_differenceFormula);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			match(DIFFERENCE);
			setState(309);
			match(T__0);
			setState(310);
			match(FACTOR);
			setState(313); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(311);
				match(T__2);
				setState(312);
				match(FACTOR);
				}
				}
				setState(315); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__2 );
			setState(317);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class YearsSinceFormulaContext extends ParserRuleContext {
		public TerminalNode YEARS_SINCE() { return getToken(Esgish2GrammarParser.YEARS_SINCE, 0); }
		public TerminalNode FACTOR() { return getToken(Esgish2GrammarParser.FACTOR, 0); }
		public YearsSinceFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_yearsSinceFormula; }
	}

	public final YearsSinceFormulaContext yearsSinceFormula() throws RecognitionException {
		YearsSinceFormulaContext _localctx = new YearsSinceFormulaContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_yearsSinceFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(319);
			match(YEARS_SINCE);
			setState(320);
			match(T__0);
			setState(321);
			match(FACTOR);
			setState(322);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BooleanFormulaContext extends ParserRuleContext {
		public TerminalNode BOOLEAN() { return getToken(Esgish2GrammarParser.BOOLEAN, 0); }
		public QueryContext query() {
			return getRuleContext(QueryContext.class,0);
		}
		public BooleanFormulaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_booleanFormula; }
	}

	public final BooleanFormulaContext booleanFormula() throws RecognitionException {
		BooleanFormulaContext _localctx = new BooleanFormulaContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_booleanFormula);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(324);
			match(BOOLEAN);
			setState(325);
			match(T__0);
			setState(326);
			query();
			setState(327);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001&\u014a\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0003\u0000J\b\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0003\u0001T\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0003"+
		"\u0002Y\b\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0003\u0003g\b\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0003\u0004l\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0003\u0005r\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u0006x\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0003"+
		"\u0007}\b\u0007\u0001\u0007\u0003\u0007\u0080\b\u0007\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0003\b\u0086\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0003\t\u008d\b\t\u0001\t\u0003\t\u0090\b\t\u0001\n\u0001\n\u0001\n"+
		"\u0001\n\u0003\n\u0096\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0003\u000b\u009c\b\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0003\r\u00a4\b\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0004\u000f\u00b1\b\u000f\u000b\u000f\f\u000f\u00b2\u0001\u000f\u0001"+
		"\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0004"+
		"\u0010\u00bc\b\u0010\u000b\u0010\f\u0010\u00bd\u0001\u0010\u0001\u0010"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00cb\b\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0003\u0013\u00dc\b\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0004\u0017\u00f8\b\u0017\u000b\u0017\f\u0017\u00f9\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0004\u001f\u012f\b\u001f\u000b\u001f\f\u001f\u0130"+
		"\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001 \u0001 \u0001 \u0004 \u013a"+
		"\b \u000b \f \u013b\u0001 \u0001 \u0001!\u0001!\u0001!\u0001!\u0001!\u0001"+
		"\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0000\u0000#\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$&(*,.02468:<>@BD\u0000\u0001\u0001\u0000$%\u015a\u0000I\u0001\u0000\u0000"+
		"\u0000\u0002S\u0001\u0000\u0000\u0000\u0004U\u0001\u0000\u0000\u0000\u0006"+
		"f\u0001\u0000\u0000\u0000\bh\u0001\u0000\u0000\u0000\nm\u0001\u0000\u0000"+
		"\u0000\fs\u0001\u0000\u0000\u0000\u000ey\u0001\u0000\u0000\u0000\u0010"+
		"\u0081\u0001\u0000\u0000\u0000\u0012\u008c\u0001\u0000\u0000\u0000\u0014"+
		"\u0091\u0001\u0000\u0000\u0000\u0016\u0097\u0001\u0000\u0000\u0000\u0018"+
		"\u009d\u0001\u0000\u0000\u0000\u001a\u00a0\u0001\u0000\u0000\u0000\u001c"+
		"\u00a7\u0001\u0000\u0000\u0000\u001e\u00ab\u0001\u0000\u0000\u0000 \u00b6"+
		"\u0001\u0000\u0000\u0000\"\u00c1\u0001\u0000\u0000\u0000$\u00ca\u0001"+
		"\u0000\u0000\u0000&\u00db\u0001\u0000\u0000\u0000(\u00dd\u0001\u0000\u0000"+
		"\u0000*\u00e4\u0001\u0000\u0000\u0000,\u00eb\u0001\u0000\u0000\u0000."+
		"\u00f0\u0001\u0000\u0000\u00000\u00fe\u0001\u0000\u0000\u00002\u0103\u0001"+
		"\u0000\u0000\u00004\u0108\u0001\u0000\u0000\u00006\u010f\u0001\u0000\u0000"+
		"\u00008\u0116\u0001\u0000\u0000\u0000:\u011f\u0001\u0000\u0000\u0000<"+
		"\u0124\u0001\u0000\u0000\u0000>\u0129\u0001\u0000\u0000\u0000@\u0134\u0001"+
		"\u0000\u0000\u0000B\u013f\u0001\u0000\u0000\u0000D\u0144\u0001\u0000\u0000"+
		"\u0000FJ\u0003\u0002\u0001\u0000GJ\u0003\u0004\u0002\u0000HJ\u0003&\u0013"+
		"\u0000IF\u0001\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000IH\u0001\u0000"+
		"\u0000\u0000JK\u0001\u0000\u0000\u0000KL\u0005\u0000\u0000\u0001L\u0001"+
		"\u0001\u0000\u0000\u0000MT\u0003\u0006\u0003\u0000NT\u0003\u001e\u000f"+
		"\u0000OT\u0003 \u0010\u0000PT\u0003\"\u0011\u0000QT\u0003\u0018\f\u0000"+
		"RT\u0003\u001c\u000e\u0000SM\u0001\u0000\u0000\u0000SN\u0001\u0000\u0000"+
		"\u0000SO\u0001\u0000\u0000\u0000SP\u0001\u0000\u0000\u0000SQ\u0001\u0000"+
		"\u0000\u0000SR\u0001\u0000\u0000\u0000T\u0003\u0001\u0000\u0000\u0000"+
		"UX\u0005\u0001\u0000\u0000VY\u0003\u0002\u0001\u0000WY\u0003\u0004\u0002"+
		"\u0000XV\u0001\u0000\u0000\u0000XW\u0001\u0000\u0000\u0000YZ\u0001\u0000"+
		"\u0000\u0000Z[\u0005\u0002\u0000\u0000[\u0005\u0001\u0000\u0000\u0000"+
		"\\g\u0003\b\u0004\u0000]g\u0003\u001c\u000e\u0000^g\u0003\n\u0005\u0000"+
		"_g\u0003\f\u0006\u0000`g\u0003\u000e\u0007\u0000ag\u0003\u0010\b\u0000"+
		"bg\u0003\u0012\t\u0000cg\u0003\u0014\n\u0000dg\u0003\u0016\u000b\u0000"+
		"eg\u0003\"\u0011\u0000f\\\u0001\u0000\u0000\u0000f]\u0001\u0000\u0000"+
		"\u0000f^\u0001\u0000\u0000\u0000f_\u0001\u0000\u0000\u0000f`\u0001\u0000"+
		"\u0000\u0000fa\u0001\u0000\u0000\u0000fb\u0001\u0000\u0000\u0000fc\u0001"+
		"\u0000\u0000\u0000fd\u0001\u0000\u0000\u0000fe\u0001\u0000\u0000\u0000"+
		"g\u0007\u0001\u0000\u0000\u0000hi\u0005\u0005\u0000\u0000ik\u0005\b\u0000"+
		"\u0000jl\u0005$\u0000\u0000kj\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000"+
		"\u0000l\t\u0001\u0000\u0000\u0000mn\u0005\u0005\u0000\u0000no\u0005\u000e"+
		"\u0000\u0000oq\u0005%\u0000\u0000pr\u0005$\u0000\u0000qp\u0001\u0000\u0000"+
		"\u0000qr\u0001\u0000\u0000\u0000r\u000b\u0001\u0000\u0000\u0000st\u0003"+
		"&\u0013\u0000tu\u0005\t\u0000\u0000uw\u0005%\u0000\u0000vx\u0005$\u0000"+
		"\u0000wv\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000x\r\u0001\u0000"+
		"\u0000\u0000yz\u0005\u0005\u0000\u0000z\u007f\u0005\u0007\u0000\u0000"+
		"{}\u0005$\u0000\u0000|{\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000"+
		"}\u0080\u0001\u0000\u0000\u0000~\u0080\u0005#\u0000\u0000\u007f|\u0001"+
		"\u0000\u0000\u0000\u007f~\u0001\u0000\u0000\u0000\u0080\u000f\u0001\u0000"+
		"\u0000\u0000\u0081\u0082\u0005\u0005\u0000\u0000\u0082\u0083\u0005\t\u0000"+
		"\u0000\u0083\u0085\u0005%\u0000\u0000\u0084\u0086\u0005$\u0000\u0000\u0085"+
		"\u0084\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086"+
		"\u0011\u0001\u0000\u0000\u0000\u0087\u0088\u0005\u0005\u0000\u0000\u0088"+
		"\u0089\u0005\u000b\u0000\u0000\u0089\u008d\u0005%\u0000\u0000\u008a\u008b"+
		"\u0005\u0005\u0000\u0000\u008b\u008d\u0005\r\u0000\u0000\u008c\u0087\u0001"+
		"\u0000\u0000\u0000\u008c\u008a\u0001\u0000\u0000\u0000\u008d\u008f\u0001"+
		"\u0000\u0000\u0000\u008e\u0090\u0005$\u0000\u0000\u008f\u008e\u0001\u0000"+
		"\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u0013\u0001\u0000"+
		"\u0000\u0000\u0091\u0092\u0005\u0005\u0000\u0000\u0092\u0093\u0005\f\u0000"+
		"\u0000\u0093\u0095\u0005%\u0000\u0000\u0094\u0096\u0005$\u0000\u0000\u0095"+
		"\u0094\u0001\u0000\u0000\u0000\u0095\u0096\u0001\u0000\u0000\u0000\u0096"+
		"\u0015\u0001\u0000\u0000\u0000\u0097\u0098\u0005\u0005\u0000\u0000\u0098"+
		"\u0099\u0005\n\u0000\u0000\u0099\u009b\u0005%\u0000\u0000\u009a\u009c"+
		"\u0005$\u0000\u0000\u009b\u009a\u0001\u0000\u0000\u0000\u009b\u009c\u0001"+
		"\u0000\u0000\u0000\u009c\u0017\u0001\u0000\u0000\u0000\u009d\u009e\u0005"+
		"\u0004\u0000\u0000\u009e\u009f\u0005\b\u0000\u0000\u009f\u0019\u0001\u0000"+
		"\u0000\u0000\u00a0\u00a3\u0005\u0001\u0000\u0000\u00a1\u00a4\u0003\u0018"+
		"\f\u0000\u00a2\u00a4\u0003\u001a\r\u0000\u00a3\u00a1\u0001\u0000\u0000"+
		"\u0000\u00a3\u00a2\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001\u0000\u0000"+
		"\u0000\u00a5\u00a6\u0005\u0002\u0000\u0000\u00a6\u001b\u0001\u0000\u0000"+
		"\u0000\u00a7\u00a8\u0005\u0006\u0000\u0000\u00a8\u00a9\u0005\t\u0000\u0000"+
		"\u00a9\u00aa\u0005%\u0000\u0000\u00aa\u001d\u0001\u0000\u0000\u0000\u00ab"+
		"\u00ac\u0005\u001e\u0000\u0000\u00ac\u00ad\u0005\u0001\u0000\u0000\u00ad"+
		"\u00b0\u0003$\u0012\u0000\u00ae\u00af\u0005\u0003\u0000\u0000\u00af\u00b1"+
		"\u0003$\u0012\u0000\u00b0\u00ae\u0001\u0000\u0000\u0000\u00b1\u00b2\u0001"+
		"\u0000\u0000\u0000\u00b2\u00b0\u0001\u0000\u0000\u0000\u00b2\u00b3\u0001"+
		"\u0000\u0000\u0000\u00b3\u00b4\u0001\u0000\u0000\u0000\u00b4\u00b5\u0005"+
		"\u0002\u0000\u0000\u00b5\u001f\u0001\u0000\u0000\u0000\u00b6\u00b7\u0005"+
		"\u001f\u0000\u0000\u00b7\u00b8\u0005\u0001\u0000\u0000\u00b8\u00bb\u0003"+
		"$\u0012\u0000\u00b9\u00ba\u0005\u0003\u0000\u0000\u00ba\u00bc\u0003$\u0012"+
		"\u0000\u00bb\u00b9\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001\u0000\u0000"+
		"\u0000\u00bd\u00bb\u0001\u0000\u0000\u0000\u00bd\u00be\u0001\u0000\u0000"+
		"\u0000\u00be\u00bf\u0001\u0000\u0000\u0000\u00bf\u00c0\u0005\u0002\u0000"+
		"\u0000\u00c0!\u0001\u0000\u0000\u0000\u00c1\u00c2\u0005 \u0000\u0000\u00c2"+
		"\u00c3\u0003\u0004\u0002\u0000\u00c3#\u0001\u0000\u0000\u0000\u00c4\u00cb"+
		"\u0003\u0006\u0003\u0000\u00c5\u00cb\u0003\u001e\u000f\u0000\u00c6\u00cb"+
		"\u0003\"\u0011\u0000\u00c7\u00cb\u0003 \u0010\u0000\u00c8\u00cb\u0003"+
		"\u0018\f\u0000\u00c9\u00cb\u0003&\u0013\u0000\u00ca\u00c4\u0001\u0000"+
		"\u0000\u0000\u00ca\u00c5\u0001\u0000\u0000\u0000\u00ca\u00c6\u0001\u0000"+
		"\u0000\u0000\u00ca\u00c7\u0001\u0000\u0000\u0000\u00ca\u00c8\u0001\u0000"+
		"\u0000\u0000\u00ca\u00c9\u0001\u0000\u0000\u0000\u00cb%\u0001\u0000\u0000"+
		"\u0000\u00cc\u00dc\u0003,\u0016\u0000\u00cd\u00dc\u0003.\u0017\u0000\u00ce"+
		"\u00dc\u00030\u0018\u0000\u00cf\u00dc\u00032\u0019\u0000\u00d0\u00dc\u0003"+
		"4\u001a\u0000\u00d1\u00dc\u00036\u001b\u0000\u00d2\u00dc\u00038\u001c"+
		"\u0000\u00d3\u00dc\u0003:\u001d\u0000\u00d4\u00dc\u0003<\u001e\u0000\u00d5"+
		"\u00dc\u0003>\u001f\u0000\u00d6\u00dc\u0003@ \u0000\u00d7\u00dc\u0003"+
		"*\u0015\u0000\u00d8\u00dc\u0003(\u0014\u0000\u00d9\u00dc\u0003B!\u0000"+
		"\u00da\u00dc\u0003D\"\u0000\u00db\u00cc\u0001\u0000\u0000\u0000\u00db"+
		"\u00cd\u0001\u0000\u0000\u0000\u00db\u00ce\u0001\u0000\u0000\u0000\u00db"+
		"\u00cf\u0001\u0000\u0000\u0000\u00db\u00d0\u0001\u0000\u0000\u0000\u00db"+
		"\u00d1\u0001\u0000\u0000\u0000\u00db\u00d2\u0001\u0000\u0000\u0000\u00db"+
		"\u00d3\u0001\u0000\u0000\u0000\u00db\u00d4\u0001\u0000\u0000\u0000\u00db"+
		"\u00d5\u0001\u0000\u0000\u0000\u00db\u00d6\u0001\u0000\u0000\u0000\u00db"+
		"\u00d7\u0001\u0000\u0000\u0000\u00db\u00d8\u0001\u0000\u0000\u0000\u00db"+
		"\u00d9\u0001\u0000\u0000\u0000\u00db\u00da\u0001\u0000\u0000\u0000\u00dc"+
		"\'\u0001\u0000\u0000\u0000\u00dd\u00de\u0005\u001b\u0000\u0000\u00de\u00df"+
		"\u0005\u0001\u0000\u0000\u00df\u00e0\u0005\u0005\u0000\u0000\u00e0\u00e1"+
		"\u0005\u0003\u0000\u0000\u00e1\u00e2\u0005\u0005\u0000\u0000\u00e2\u00e3"+
		"\u0005\u0002\u0000\u0000\u00e3)\u0001\u0000\u0000\u0000\u00e4\u00e5\u0005"+
		"\u001a\u0000\u0000\u00e5\u00e6\u0005\u0001\u0000\u0000\u00e6\u00e7\u0005"+
		"\u0005\u0000\u0000\u00e7\u00e8\u0005\u0003\u0000\u0000\u00e8\u00e9\u0005"+
		"\u0005\u0000\u0000\u00e9\u00ea\u0005\u0002\u0000\u0000\u00ea+\u0001\u0000"+
		"\u0000\u0000\u00eb\u00ec\u0005\u000f\u0000\u0000\u00ec\u00ed\u0005\u0001"+
		"\u0000\u0000\u00ed\u00ee\u0003\u0002\u0001\u0000\u00ee\u00ef\u0005\u0002"+
		"\u0000\u0000\u00ef-\u0001\u0000\u0000\u0000\u00f0\u00f1\u0005\u0010\u0000"+
		"\u0000\u00f1\u00f7\u0005\u0001\u0000\u0000\u00f2\u00f3\u0003\u0006\u0003"+
		"\u0000\u00f3\u00f4\u0005\u0003\u0000\u0000\u00f4\u00f5\u0007\u0000\u0000"+
		"\u0000\u00f5\u00f6\u0005\u0003\u0000\u0000\u00f6\u00f8\u0001\u0000\u0000"+
		"\u0000\u00f7\u00f2\u0001\u0000\u0000\u0000\u00f8\u00f9\u0001\u0000\u0000"+
		"\u0000\u00f9\u00f7\u0001\u0000\u0000\u0000\u00f9\u00fa\u0001\u0000\u0000"+
		"\u0000\u00fa\u00fb\u0001\u0000\u0000\u0000\u00fb\u00fc\u0007\u0000\u0000"+
		"\u0000\u00fc\u00fd\u0005\u0002\u0000\u0000\u00fd/\u0001\u0000\u0000\u0000"+
		"\u00fe\u00ff\u0005\u0011\u0000\u0000\u00ff\u0100\u0005\u0001\u0000\u0000"+
		"\u0100\u0101\u0003\u0002\u0001\u0000\u0101\u0102\u0005\u0002\u0000\u0000"+
		"\u01021\u0001\u0000\u0000\u0000\u0103\u0104\u0005\u0013\u0000\u0000\u0104"+
		"\u0105\u0005\u0001\u0000\u0000\u0105\u0106\u0005\u0005\u0000\u0000\u0106"+
		"\u0107\u0005\u0002\u0000\u0000\u01073\u0001\u0000\u0000\u0000\u0108\u0109"+
		"\u0005\u0012\u0000\u0000\u0109\u010a\u0005\u0001\u0000\u0000\u010a\u010b"+
		"\u0005\u0005\u0000\u0000\u010b\u010c\u0005\u0003\u0000\u0000\u010c\u010d"+
		"\u0005\u0005\u0000\u0000\u010d\u010e\u0005\u0002\u0000\u0000\u010e5\u0001"+
		"\u0000\u0000\u0000\u010f\u0110\u0005\u0014\u0000\u0000\u0110\u0111\u0005"+
		"\u0001\u0000\u0000\u0111\u0112\u0005\u0005\u0000\u0000\u0112\u0113\u0005"+
		"\u0003\u0000\u0000\u0113\u0114\u0005%\u0000\u0000\u0114\u0115\u0005\u0002"+
		"\u0000\u0000\u01157\u0001\u0000\u0000\u0000\u0116\u0117\u0005\u0015\u0000"+
		"\u0000\u0117\u0118\u0005\u0001\u0000\u0000\u0118\u0119\u0005\u0005\u0000"+
		"\u0000\u0119\u011a\u0005\u0003\u0000\u0000\u011a\u011b\u0005\u0005\u0000"+
		"\u0000\u011b\u011c\u0005\u0003\u0000\u0000\u011c\u011d\u0005%\u0000\u0000"+
		"\u011d\u011e\u0005\u0002\u0000\u0000\u011e9\u0001\u0000\u0000\u0000\u011f"+
		"\u0120\u0005\u0016\u0000\u0000\u0120\u0121\u0005\u0001\u0000\u0000\u0121"+
		"\u0122\u0005\u0005\u0000\u0000\u0122\u0123\u0005\u0002\u0000\u0000\u0123"+
		";\u0001\u0000\u0000\u0000\u0124\u0125\u0005\u0017\u0000\u0000\u0125\u0126"+
		"\u0005\u0001\u0000\u0000\u0126\u0127\u0005\u0005\u0000\u0000\u0127\u0128"+
		"\u0005\u0002\u0000\u0000\u0128=\u0001\u0000\u0000\u0000\u0129\u012a\u0005"+
		"\u0018\u0000\u0000\u012a\u012b\u0005\u0001\u0000\u0000\u012b\u012e\u0005"+
		"\u0005\u0000\u0000\u012c\u012d\u0005\u0003\u0000\u0000\u012d\u012f\u0005"+
		"\u0005\u0000\u0000\u012e\u012c\u0001\u0000\u0000\u0000\u012f\u0130\u0001"+
		"\u0000\u0000\u0000\u0130\u012e\u0001\u0000\u0000\u0000\u0130\u0131\u0001"+
		"\u0000\u0000\u0000\u0131\u0132\u0001\u0000\u0000\u0000\u0132\u0133\u0005"+
		"\u0002\u0000\u0000\u0133?\u0001\u0000\u0000\u0000\u0134\u0135\u0005\u0019"+
		"\u0000\u0000\u0135\u0136\u0005\u0001\u0000\u0000\u0136\u0139\u0005\u0005"+
		"\u0000\u0000\u0137\u0138\u0005\u0003\u0000\u0000\u0138\u013a\u0005\u0005"+
		"\u0000\u0000\u0139\u0137\u0001\u0000\u0000\u0000\u013a\u013b\u0001\u0000"+
		"\u0000\u0000\u013b\u0139\u0001\u0000\u0000\u0000\u013b\u013c\u0001\u0000"+
		"\u0000\u0000\u013c\u013d\u0001\u0000\u0000\u0000\u013d\u013e\u0005\u0002"+
		"\u0000\u0000\u013eA\u0001\u0000\u0000\u0000\u013f\u0140\u0005\u001c\u0000"+
		"\u0000\u0140\u0141\u0005\u0001\u0000\u0000\u0141\u0142\u0005\u0005\u0000"+
		"\u0000\u0142\u0143\u0005\u0002\u0000\u0000\u0143C\u0001\u0000\u0000\u0000"+
		"\u0144\u0145\u0005\u001d\u0000\u0000\u0145\u0146\u0005\u0001\u0000\u0000"+
		"\u0146\u0147\u0003\u0002\u0001\u0000\u0147\u0148\u0005\u0002\u0000\u0000"+
		"\u0148E\u0001\u0000\u0000\u0000\u0016ISXfkqw|\u007f\u0085\u008c\u008f"+
		"\u0095\u009b\u00a3\u00b2\u00bd\u00ca\u00db\u00f9\u0130\u013b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}