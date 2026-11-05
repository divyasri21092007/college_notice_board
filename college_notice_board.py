
import 'package:flutter/material.dart';

void main() {
  runApp(const CollegeNoticeBoard());
}

class CollegeNoticeBoard extends StatelessWidget {
  const CollegeNoticeBoard({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'College Notice Board',
      theme: ThemeData(
        colorSchemeSeed: Colors.indigo,
        useMaterial3: true,
      ),
      home: const LoginPage(),
    );
  }
}

// LOGIN PAGE
class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();

  void login() {
    if (emailController.text.trim().isEmpty ||
        passwordController.text.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Please enter email and password'),
        ),
      );
      return;
    }

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (_) => const HomePage(),
      ),
    );
  }

  @override
  void dispose() {
    emailController.dispose();
    passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.indigo.shade50,
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(25),
          child: Card(
            elevation: 5,
            child: Padding(
              padding: const EdgeInsets.all(25),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Icon(
                    Icons.campaign,
                    size: 75,
                    color: Colors.indigo,
                  ),
                  const SizedBox(height: 15),
                  const Text(
                    'College Notice Board',
                    style: TextStyle(
                      fontSize: 25,
                      fontWeight: FontWeight.bold,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 25),
                  TextField(
                    controller: emailController,
                    decoration: const InputDecoration(
                      labelText: 'Email / Student ID',
                      prefixIcon: Icon(Icons.person),
                      border: OutlineInputBorder(),
                    ),
                  ),
                  const SizedBox(height: 15),
                  TextField(
                    controller: passwordController,
                    obscureText: true,
                    decoration: const InputDecoration(
                      labelText: 'Password',
                      prefixIcon: Icon(Icons.lock),
                      border: OutlineInputBorder(),
                    ),
                  ),
                  const SizedBox(height: 20),
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      onPressed: login,
                      child: const Text('Login'),
                    ),
                  ),
                  const Text(
                    'Demo login: Enter any email and password',
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}

// NOTICE MODEL
class Notice {
  final String title;
  final String description;
  final String category;
  final DateTime date;

  Notice({
    required this.title,
    required this.description,
    required this.category,
    required this.date,
  });
}

// HOME PAGE
class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final List<Notice> notices = [
    Notice(
      title: 'Welcome to College Notice Board',
      description: 'Stay updated with all college announcements.',
      category: 'General',
      date: DateTime.now(),
    ),
    Notice(
      title: 'Internal Examination',
      description: 'Internal examinations will begin next Monday.',
      category: 'Examination',
      date: DateTime.now(),
    ),
    Notice(
      title: 'Technical Fest',
      description: 'Students can register for the upcoming technical fest.',
      category: 'Events',
      date: DateTime.now(),
    ),
    Notice(
      title: 'Library Timings',
      description: 'The library will remain open until 6 PM.',
      category: 'General',
      date: DateTime.now(),
    ),
  ];

  String selectedCategory = 'All';

  List<Notice> get filteredNotices {
    if (selectedCategory == 'All') {
      return notices;
    }

    return notices
        .where((n) => n.category == selectedCategory)
        .toList();
  }

  void addNotice() {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (_) => AddNoticePage(
          onAdd: (notice) {
            setState(() {
              notices.insert(0, notice);
            });
          },
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final categories = [
      'All',
      'General',
      'Examination',
      'Events',
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text('College Notice Board'),
        backgroundColor: Colors.indigo,
        foregroundColor: Colors.white,
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () {
              Navigator.pushReplacement(
                context,
                MaterialPageRoute(
                  builder: (_) => const LoginPage(),
                ),
              );
            },
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: addNotice,
        icon: const Icon(Icons.add),
        label: const Text('Add Notice'),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(20),
            color: Colors.indigo.shade50,
            child: const Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Hello, Student! 👋',
                  style: TextStyle(
                    fontSize: 23,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                SizedBox(height: 5),
                Text(
                  'Check the latest college announcements.',
                ),
              ],
            ),
          ),
          const Padding(
            padding: EdgeInsets.all(16),
            child: Text(
              'Notice Categories',
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          SizedBox(
            height: 45,
            child: ListView(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 12),
              children: categories.map((category) {
                return Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 4),
                  child: ChoiceChip(
                    label: Text(category),
                    selected: selectedCategory == category,
                    onSelected: (_) {
                      setState(() {
                        selectedCategory = category;
                      });
                    },
                  ),
                );
              }).toList(),
            ),
          ),
          const Padding(
            padding: EdgeInsets.all(16),
            child: Text(
              'Latest Notices',
              style: TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          Expanded(
            child: filteredNotices.isEmpty
                ? const Center(
                    child: Text('No notices available'),
                  )
                : ListView.builder(
                    padding: const EdgeInsets.fromLTRB(
                      12, 0, 12, 80,
                    ),
                    itemCount: filteredNotices.length,
                    itemBuilder: (context, index) {
                      final notice = filteredNotices[index];

                      return Card(
                        margin: const EdgeInsets.only(bottom: 12),
                        child: ListTile(
                          leading: CircleAvatar(
                            backgroundColor: Colors.indigo.shade100,
                            child: Icon(
                              notice.category == 'Examination'
                                  ? Icons.assignment
                                  : notice.category == 'Events'
                                      ? Icons.event
                                      : Icons.campaign,
                              color: Colors.indigo,
                            ),
                          ),
                          title: Text(
                            notice.title,
                            style: const TextStyle(
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          subtitle: Text(
                            '${notice.category} • '
                            '${notice.date.day}/'
                            '${notice.date.month}/'
                            '${notice.date.year}',
                          ),
                          trailing: const Icon(
                            Icons.arrow_forward_ios,
                            size: 16,
                          ),
                          onTap: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (_) =>
                                    NoticeDetailsPage(
                                  notice: notice,
                                ),
                              ),
                            );
                          },
                        ),
                      );
                    },
                  ),
          ),
        ],
      ),
    );
  }
}

// NOTICE DETAILS PAGE
class NoticeDetailsPage extends StatelessWidget {
  final Notice notice;

  const NoticeDetailsPage({
    super.key,
    required this.notice,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Notice Details'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(22),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              notice.category.toUpperCase(),
              style: const TextStyle(
                color: Colors.indigo,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 15),
            Text(
              notice.title,
              style: const TextStyle(
                fontSize: 25,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 15),
            Text(
              '${notice.date.day}/'
              '${notice.date.month}/'
              '${notice.date.year}',
              style: const TextStyle(color: Colors.grey),
            ),
            const Divider(height: 30),
            Text(
              notice.description,
              style: const TextStyle(fontSize: 18),
            ),
          ],
        ),
      ),
    );
  }
}

// ADD NOTICE PAGE
class AddNoticePage extends StatefulWidget {
  final Function(Notice) onAdd;

  const AddNoticePage({
    super.key,
    required this.onAdd,
  });

  @override
  State<AddNoticePage> createState() => _AddNoticePageState();
}

class _AddNoticePageState extends State<AddNoticePage> {
  final titleController = TextEditingController();
  final descriptionController = TextEditingController();

  String category = 'General';

  void saveNotice() {
    if (titleController.text.trim().isEmpty ||
        descriptionController.text.trim().isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Please fill all fields'),
        ),
      );
      return;
    }

    widget.onAdd(
      Notice(
        title: titleController.text.trim(),
        description: descriptionController.text.trim(),
        category: category,
        date: DateTime.now(),
      ),
    );

    Navigator.pop(context);
  }

  @override
  void dispose() {
    titleController.dispose();
    descriptionController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Add New Notice'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            TextField(
              controller: titleController,
              decoration: const InputDecoration(
                labelText: 'Notice Title',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 18),
            TextField(
              controller: descriptionController,
              maxLines: 5,
              decoration: const InputDecoration(
                labelText: 'Notice Description',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 18),
            DropdownButtonFormField<String>(
              initialValue: category,
              decoration: const InputDecoration(
                labelText: 'Category',
                border: OutlineInputBorder(),
              ),
              items: [
                'General',
                'Examination',
                'Events',
              ].map((c) {
                return DropdownMenuItem<String>(
                  value: c,
                  child: Text(c),
                );
              }).toList(),
              onChanged: (value) {
                if (value != null) {
                  setState(() {
                    category = value;
                  });
                }
              },
            ),
            const SizedBox(height: 25),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton.icon(
                onPressed: saveNotice,
                icon: const Icon(Icons.save),
                label: const Text('Publish Notice'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
